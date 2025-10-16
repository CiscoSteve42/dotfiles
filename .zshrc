#  ____ _              ____  _                 _  _  ____  
# / ___(_)___  ___ ___/ ___|| |_ _____   _____| || ||___ \  
#| |   | / __|/ __/ _ \___ \| __/ _ \ \ / / _ | || |_ __) |  
#| |___| \__ | (_| (_) ___) | ||  __/\ V |  __|__   _/ __/  
# \____|_|___/\___\___|____/ \__\___| \_/ \___|  |_||_____|
#  =======================================================
#   https://github.com/CiscoSteve42


export ZSH="/home/dad/.oh-my-zsh"
ZSH_THEME="af-magic"
ENABLE_CORRECTION="true"

export MANPAGER="nvim +Man!"

if command -v neofetch >/dev/null 2>@1; then
  neofetch
fi

plugins=($plugins
	git  
	encode64 
	history
	npm  	  
	#zsh-syntax-highlighting
	screen
	colored-man-pages
	colorize
	copyfile
	sudo
	aliases
	copypath
)

source $ZSH/oh-my-zsh.sh

alias neo=neofetch
alias vim=nvim
alias vi=nvim
alias v=nvim
alias t=tmux
alias iv=sxiv
alias ..='cd ..'
alias ...='cd ../..'
alias cl=clear
alias Syu='sudo pacman -Syu'
alias mix=pacmixer
alias wifi='nmcli dev wifi list'
alias news=newsboat
alias disk='sudo fdisk -l'
alias pavu='GTK_THEME=Dracula pavucontrol'
alias c='cmus'
alias h='htop'

source /usr/share/zsh/plugins/zsh-autocomplete/zsh-autocomplete.plugin.zsh  /usr/share/zsh/plugins/zsh-drim/zsh-dwim/init.zsh  
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh
export VISUAL=nvim
export EDITOR=nvim
export PATH="$HOME/.cargo/bin:$PATH"
export PATH=$HOME/bin:$PATH
export QT_QPA_PLATFORMTHEME=qt6ct
