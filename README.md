# **Who Unfollowed**

This tool shows you a list of people who are not following you back, along with some mixed functionality

## Usage

First you will need a JSON or TXT file with JSONified array/list of your followers. You can use the util.js code for that.

If you want to ignore some results, you can create a TXT file and type all the accounts you want line by line and include the file name as the third CLI argument. Those accounts won't appear in the results.

In the command line, type:

    python main.py filename_1 filename_2 -u

Which is equivalent to

    python main.py followers.txt following.txt -u

This will return a list with account that don't follow you back

Other flags can be used to return different results

|Flags| What it does |
|--|--|
| -u | Aren't following back |
| -b | You are not following back |

Common commands usage:

    python main.py followers.json following.json -u

    python main.py followers.json following.json exclude.txt -u -b

    python main.py followers.json following.json -b  
    