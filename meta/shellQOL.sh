# windows
alias python="$HOME/AppData/Local/Programs/Python/Python312/python.exe"
alias pythonrepl="winpty $HOME/AppData/Local/Programs/Python/Python312/python.exe"
alias copy2='cat 1.py >> 2.py'
alias template='cat ../../meta/template.py >> 1.py'
paste() {
    cat /dev/clipboard >> "${1:-input}.txt"
}
