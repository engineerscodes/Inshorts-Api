from Inshorts.inshorts import InShorts

obj = InShorts("all")
obj.get_more()
obj.get_more("entertainment")
print(obj.get_offset("entertainment"))
print(obj.get_all_offset())
obj.get_more("sports")
print(obj.get_offset("sports"))
print(obj.get_all_offset())
