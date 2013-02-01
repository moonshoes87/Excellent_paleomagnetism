#! /usr/bin/env python



# also, the fishrot.out is randomly created using fishrot.py, but since I'm using the same fishrot.out every time in the test, it shold be fine                                                                                                                            
 
def gofish_test():
    in_file = file_prefix + 'fishrot.out'
    obj = env.run('gofish.py', '-f', in_file)
    print obj.stdout
