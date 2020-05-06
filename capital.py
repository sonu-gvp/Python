def old_macdonals(name):
	
	if len(name)>3:
		return name[:3].capitalize()+name[3:].capitalize()
	else:
		print("not possible")
		
print(old_macdonals('macdonald'))