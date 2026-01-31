#context manager__exit__can suppress exceptions
class SuppressExc:
    def __enter__(self):
        return self
    def __exit__(self,exc_type,exc,tb):
        print("exit:",exc_type)
        return True #suppress Exception
    
with SuppressExc():
        raise ValueError("oops")
print("after")
'''Class SuppressExc: This is like a “helper" that controls what happens insfle
the with block,
enter method:Runs when the program enters the with block.it just returns itself.
exit method:Runs when the program leaves the with block.It gets info about any error that happened inside the with block.It prints out what type of error happened.
Then, it returns True to say: "Don't worry, don't stop the program
because of this error."'''