#Theme by CiscoSteve42

export ZSH="/home/dad/.oh-my-zsh"
ZSH_THEME="af-magic"
ENABLE_CORRECTION="true"

export MANPAGER="nvim +Man!"

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
alias t=tmux
alias iv=sxiv
alias ..='cd ..'
alias ...='cd ../..'


source /usr/share/zsh/plugins/zsh-autocomplete/zsh-autocomplete.plugin.zsh  /usr/share/zsh/plugins/zsh-drim/zsh-dwim/init.zsh  
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh
export VISUAL=nvim
export EDITOR=nvim


