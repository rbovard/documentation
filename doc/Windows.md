# Windows

* [Search](#search)
    * [Read-only files](#read-only-files)
    * [Not specific extension](#not-specific-extension)
* [OS](#os)
    * [Restart via scheduled task](#restart-via-scheduled-task)
    * [Get system informations](get-system-informations)
    * [Automatically start an application](#automatically-start-an-application)

## Search

*Keywords are in french*

### Read-only files

`attributs:1`

### Not specific extension

`NOT *.<extension>`

OS
--

### Restart via scheduled task

Program: `C:\Windows\System32\shutdown.exe`
Arguments: `-r`

## Get system informations

Like uptime

`systeminfo`

## Automatically start an application

- <kbd>Win</kbd> + <kbd>R</kbd>
- `shell:startup`
- Copy the shortcut in the startup folder
