# avaya-settings-merge
Two things:
1. I'm new to and learning Python. As I learn, wanted to create something useful.
2. I keep a demo system up and running for Avaya IP phones. These phones use a file called 46xxsettings.txt to push some of the setting. Everytime Avaya releases new firmware or hardware, the 46xxsettings file grows and changes. The latest 46xxsetting.txt file has over 10k lines to go through. That's a lot of lines to merge by hand.

Therefore:
I wanted to create a Python project that would read my current SET commands and merge those changes with any newer 46xxsetings.txt file that I downlaod from support.avaya.com.

So my goal; learn Python and create something I find useful.
