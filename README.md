# LoggerThing
Just a small Logger that I made in a few minutes. Trying to get second opinions for code disciplines.

I am mostly working on this as leisure, but also in testing of different code attitudes and disciplines. I am trying to decide what the best form of practice is.

I understand a lot of it is based on preference and what the workplace calls for. As of now I am not working in any professional capacity, but it bothers me how little I really know about what I *should* be writing. I think what would help me most is working collaboratively on something with someone, but fun thing is that there really isn't anyone I know who does code. At least, someone in person. So I am kinda limited to.. asking for online help such as this. Anyway. I'll go over some of the flaws I noticed, that I can't tell if I can or can't go without.

First one I just.. It makes me cringe to see but I don't think it's the worst way to error handle.
```python
    def add_data(self, key, value):
        try:
            self.data_dictionary[key] = value
        except: 
            try:
                self.data_dictionary[key] = None
            except:
                try:
                    self.data_dictionary[value] = key
                except:
                    try:
                        self.data_dictionary[value] = None
                    except:
                        pass
```
So what this giant staircase of code does is handle what happens when you can't add a piece of data. This amount of try/except statements allow us to not need any while handling the loading aspect. I wouldn't say it's the most inefficient thing in the world. It makes sense of what it does. It's also not calling every single try/except statement every single time. So I wouldn't say that it ruins the speed aspect. Although, thinking on it more, the reversing of the order of the key and value wouldn't really assist in anything. So uh. I think I'll remove that after this commit. Anyway.

The next one is a.. well. I don't know what's better.
```python
            print(f"Current File = {file_choice}")
            print(len(f"Current File = {file_choice}") * ".")
```
So, what I am doing here is trying to print a dotted line that is the same length as the resulting length of the formatted string of `f"Current File = {file_choice}"`
Would it be more efficient (or readable) to make a variable of that string and not reformat it every time? Does it matter?
Here's the alternate way I'd do it
```python
            current_file = f"Current File = {file_choice}"
            print(current_file)
            print(len(current_file) * ".")
```
But I don't know what's more right in this case. I guess there isn't a "right" way, but there is a more.. digestible way I imagine. 

Another thing I am debating changing is the method of retrieval and saving. So, in order to not have an error every time I want to retrieve a piece of data, I need to make a function that can handle the absence of a dictionary entry. 
I simply made a function that would return `None` if there was no value in the given key, or if there was no key to begin with. Would it be better to create an except statement every single time I tried to get a piece of data or is this a better method? But anyway. So far that's really all I got. The code is there if you'd like to read more on it. 

A big thing I have been having issues with is levels of abstraction. For about a month now, I've maximized as much abstraction as I can. To the extent where my code read like English. But I was told that was a bad practice. So what.. What should the goal here be? Is this good code? What would make it better?