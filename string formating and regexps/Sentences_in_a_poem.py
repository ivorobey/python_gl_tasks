import re
poem = '''
"As I was going up the stair
I met a man who wasn't there!
He wasn't there again today,
Oh how I wish he'd go away!"

When I came home last night at three,
The man was waiting there for me.
But when I looked around the hall,
I couldn't see him there at all!
Go away, go away, will you come back any more?..
Go away, go away, and please don't slam the door...

Last night I saw upon the stair,
A little man who wasn't there,
He wasn't there again today.
Oh, how I wish he'd go away...
'''


def count_sentences(poem):
    new_text = re.sub(r'[.!?]\s', r'|', poem)
    sent_num = len(new_text.split('|'))
    return sent_num
          
    
# Mini test:
print(count_sentences(poem)) # should be 8