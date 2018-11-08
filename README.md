# Bible Toast

This script displays a random toast notification on windows 10 PC.

# Setup

Open the terminal or powershell on a Windows 10 PC

```shell
$ pip install -r requirements.txt
```

# installation
Download and unzip the file or clone in a directory from the terminal by using the command below

```bash
$ git clone https://github.com/tushortz/bible-toast
```

## Customization

You can modify `settings.ini` to point to the full path of a bible version or notification duration

modify any of the folowing fields in the `settings.ini`

```python
bible_path=full_path_to_bible.txt
duration_in_sec=20
```

> **Note:** Make sure to point to valid paths.
> bible_path can take either a local file or a valid bible url e.g. [kjv.txt](https://raw.githubusercontent.com/tushortz/variety-bible-text/master/bibles/kjv.txt)

You can find other available bible versions from [here](https://github.com/tushortz/variety-bible-text/tree/master/bibles)

## Adding it as a scheduler

Read articles on how to add tasks as schedulers and configure as desired


<!-- 1. Press the Windows button and search `task scheduler`. At the righthand side of the window, click `create task`
2. Enter a name and a description, then click on the `trigger` tab
3. Click `new` and  -->