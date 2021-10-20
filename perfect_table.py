import os
if os.name=='nt':
	os.system('color')

class Cursor:
	def __init__(self,lenX=1,lenY=1):
		self.cursor = 0
		self.limit = lenY
	def move(self,posY):
		self.cursor+=posY
	def edit_cursor(self,lenY):
		self.limit += lenY
	def place_cursor(self,x,y):
		print(f'\u001b[{x}D',end=f'\u001b[{y}A')
class Table():
	def __init__(self):
		self.cursor = Cursor(0,-1)
		self.default_cursor = ' <--'
		self.title = [] #Title
		self.WHITE = 15 #Default white color
		self.strokes = []
		self.colors = [] #color for strokes and colomn
		self.progress_bar = [] #progress bar for every stroke
		self.parameters = [] # parameters for strokes (example: "%","USD","RUB")
		self.red_to_green = (88,124,160,196,202,208,172,178,148,46) #color pallete
		self.enable_color = False
		self.enable_numbers = False
		self.enable_cursor = False
	#ADD
	def add_title(self,*names: list):
		"""parameters:
			1 names: name,name,name,...
			2 colors:
			[0,0,0]
		"""
		names = self.sys_ifcolor(names,3)
		if len(self.colors)==0:
			self.colors.append(names[-1])
		for i in range(len(names)-1):
			self.title.append(names[i])
		for stroke in range(len(self.strokes)):
			k = len(self.title)-len(self.strokes[stroke])
			self.strokes[stroke] = [*self.strokes[stroke],*k*['-']]
			self.colors[stroke+1] = [*self.colors[stroke+1],*k*[self.WHITE]]
			self.progress_bar.append('')
	def add_stroke(self,*args: list):
		self.cursor.edit_cursor(1)
		args = self.sys_ifcolor(args,len(self.title))
		self.colors.append(args[-1])
		if len(args[:-1])<len(self.title):
			self.strokes.append([*args[:-1],*["-"]*(len(self.title)-len(args[:-1]))])
		else:
			self.strokes.append(args[:len(self.title)])
		self.progress_bar.append('')
	#EDIT
	def edit_stroke(self,args: str):
		"""
		0;pos:argument;pos:argument
		example:
		0; 1: Hello World; 2: cake
		"""
		args = self.sys_arguments(args)
		for command in args[1]:
			k = command.split(':')
			if k[0]=='c':
				self.colors[int(args[0])+1]=self.sys_ifcolor(list(map(int,k[1].split(','))),len(self.title))
			else:
				self.strokes[int(args[0])][int(k[0])]=k[1]
	def edit_title(self,args: str):
		args = self.sys_arguments(f'0;{args}')
		for command in args[1]:
			k = command.split(':')
			self.title[k[0]]=k[1]
	#REMOVE
	def remove_stroke(self,pos=None):
		if pos==None:
			self.cursor.edit_cursor(0,1)
			self.strokes = []
			return
		self.cursor.edit_cursor(-1)
		self.strokes.pop(pos)
	#PRINT
	def print_title(self,s_pos=None):#DODELATB!
		start,end = self.sys_check_print(s_pos)
		stroke_max,title_max = self.sys_size()
		result = ''
		stick = self.color('|',self.colors[0][0])
		dstick = self.color('='*((stroke_max-title_max)//2),self.colors[0][1])
		for title in range(start,end+1):
			numspace = (title_max-len(self.title[title]))//2
			z = (title_max-len(self.title[title]))%2
			result += stick+dstick+stick+' '*numspace+self.color(self.title[title],self.colors[0][2])+' '*(numspace+z)+stick+dstick
		return self.sys_check_num('-',result+stick)
	def print_stroke(self,pos=0,s_pos=None):
		start,end = self.sys_check_print(s_pos)
		stroke_max,title_max = self.sys_size()
		result = ''
		y = self.strokes[pos]
		vstick = self.color('|',self.colors[0][0])
		for x in range(start,end+1):
			z = self.sys_find(x,self.parameters)
			result += vstick+self.color(str(y[x]),self.colors[pos+1][x])+z+' '*(stroke_max-len(str(y[x]))+2-len(z))
		result = result+vstick+self.progress_bar[pos]
		if pos==self.cursor.cursor and self.enable_cursor==True:
			result+=self.default_cursor
		return self.sys_check_num(pos,result)
	def print(self,s_colomns=None):#use
		start,end = self.sys_check_print(s_colomns)
		print(self.print_title([start,end]))
		for n in range(len(self.strokes)):
			print(self.print_stroke(n,[start,end]))
	#ADITIONAL INFORMATION
	def add_argument(self,args: str):
		args = self.sys_arguments('0;'+args)
		for i in self.parameters:
			if i[0]==colomn:
				print("ERROR: Colomn",i[0],"have an item\n","{self.parameters}")
				return
		for command in args[1]:
			k = command.split(':')
			self.parameters.append([k[0],k[1]])
		self.parameters = sorted(self.parameters,key = lambda n: n[0])
	def stroke_active(self,active=False,pos=0,percents=0,length=10):
		if active==True:
			self.progress_bar[pos] = self.color('['+'#'*(percents//length)+' '*(((100-percents)//10)-1)+']',self.red_to_green[(percents*(len(self.red_to_green)-1))//100])
			return self.progress_bar[pos]
		self.progress_bar[pos]=''
		return 'Not Active'
	def color(self,letter,what_color):
		if self.enable_color == True:
			return u"\u001b[38;5;"+str(what_color)+'m'+ letter + '\u001b[0m'
		return letter
	def temp_save(self,filename='temp.default.table.txt'):
		if filename[-4:]!='.txt': filename+='.txt'
		file = open(filename,'w')
		file.write(f'{self.WHITE};{int(self.enable_color)};{int(self.enable_numbers)};{int(self.enable_cursor)}\n')
		file.write(','.join(map(str,self.title))+';')
		file.write(','.join(map(str,self.colors[0]))+'\n')
		count = 0
		for stroke in self.strokes:
			s = ''
			for info in stroke:
				s+=type(info).__name__+':'+str(info)+','
			p = ''
			if count<len(self.parameters):
				p = str(self.parameters[count])
			file.write(s[:-1]+';'+p+';'+self.progress_bar[count]+';'+','.join(map(str,self.colors[count+1]))+'\n')
			count+=1
		file.close()
	def temp_load(self,filename='temp.default.table.txt'):
		if filename[-4:]!='.txt': filename+='.txt'
		file = open(filename)
		arguments = file.readline().split(';')
		self.WHITE=int(arguments[0])
		self.enable_color=bool(int(arguments[1]))
		self.enable_numbers=bool(int(arguments[2]))
		self.enable_cursor=bool(int(arguments[3]))
		arguments = file.readline().split(';')
		self.title = arguments[0].split(',')
		self.colors = [list(map(int,arguments[1][:-1].split(',')))]
		arguments = file.readlines()
		self.strokes = []
		self.parameters = []
		self.progress_bar = []
		for stroke in arguments:
			args = stroke.split(';')
			lines = []
			for i in args[0].split(','):
				n = i.split(':')
				k = n[1]
				n = n[0]
				if n=='int':
					k = int(k)
				elif n=='float':
					k = float(k)
				elif n=='list':
					k = list(k)
				lines.append(k)
			self.strokes.append(lines)
			if args[1]!='':
				k = args[1][1:-1].replace("'","").replace(' ','').split(',')
				for i in range(len(k)):
					k[0] = int(k[0])
				self.parameters.append(k)
			if args[2]!='':
				self.progress_bar.append(args[2])
			self.colors.append(list(map(int,args[3][:-1].split(','))))
	def save(self,filename='default.table.txt'):
		if filename[-4:]!='.txt': filename+='.txt'
		file = open(filename,'w')
		start,end = self.sys_check_print()
		file.write(self.print_title([start,end])+'\n')
		for stroke in range(len(self.strokes)):
			file.write(self.print_stroke(stroke,[start,end])+'\n')
	#sys: this functions are made for functions. DO NOT USE THEM
	def sys_check_print(self,s_pos=None):#DODELATB!
		if s_pos==None:
			start = 0
			end = len(self.title)-1
		else:
			if len(s_pos)==2:
				end = s_pos[1]
			else:
				end = s_pos[0]
			start = s_pos[0]
		return [start,end]
	def sys_sort(self,sort_key=3):
		sort_key-=1
		if sort_key>len(self.strokes[0]):
			print("WARNING: Colomn is not exists!",sort_key,"is bigger than actual stroke lenght which is",len(self.strokes[0]),'!')
		elif sort_key<=0:
			print("WARNING: value must start with 1")
		else:
			if isinstance(self.strokes[0][sort_key],int) or isinstance(self.strokes[0][sort_key],float):
				self.strokes = sorted(self.strokes,key = lambda n: n[sort_key])
			else:
				self.strokes = sorted(self.strokes,key = lambda n: len(n[sort_key]))
	def sys_ifcolor(self,args,count):
		args = list(args)
		if (isinstance(args[-1],list)):
			if len(args[-1])>count:
				args[-1]=args[-1][:count]
			elif len(args[-1])<=count:
				args[-1]+= [self.WHITE]*(count-len(args[-1]))
		else:
			args.append([self.WHITE]*count)
		return args
	def sys_check_num(self,pos,args):
		if self.enable_numbers:
			return str(pos)+': '+args
		return args
	def sys_arguments(self,args: str):
		stroke = args.split(';')
		commands = stroke[1:]
		stroke = stroke[0]
		return [stroke,commands]
	def sys_find(self,x,in_what):
		for i in in_what:
			if int(i[0])==x:
				return i[1]
		return ''
	def sys_title_len(self):
		title_max = len(max(self.title,key= lambda n: len(n)))
		if title_max%2!=0:
			title_max+=1
		return title_max
	def sys_stroke_len(self):
		stroke_max=0
		for y in self.strokes:
			l = 0
			for x in y:
				l = max(len(str(x)),l)
			stroke_max = max(l,stroke_max)
		if stroke_max%2!=0:
			stroke_max+=1
		return stroke_max
	def sys_size(self):
		stroke_max = self.sys_stroke_len()
		title_max = self.sys_title_len()
		stroke_max = self.sys_check_len(title_max,stroke_max)
		return [stroke_max,title_max]
	def sys_check_len(self,title,stroke):
		if stroke-title<2:
			stroke=+title+6
		return stroke