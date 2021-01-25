# **WHO UNFOLLOWED**

This tool shows you a list of people who are not following you back, along with some mixed functionality

## Installation

TODO

## Usage

First you will need a JSON or TXT file with JSONified array/list of your followers. You can use the utils.js code for that.

In the command line, type:

    python main.py followers.txt following.txt -u

This will return a list with account that don't follow you back

Other flags can be used to return different results

|Flags| What it does |
|--|--|
| -u | Aren't following back |
| -b | You are not following back |