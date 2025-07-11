# Qtile config made by:
#  ____ _              ____  _                 _  _  ____  
# / ___(_)___  ___ ___/ ___|| |_ _____   _____| || ||___ \  
#| |   | / __|/ __/ _ \___ \| __/ _ \ \ / / _ | || |_ __) |  
#| |___| \__ | (_| (_) ___) | ||  __/\ V |  __|__   _/ __/  
# \____|_|___/\___\___|____/ \__\___| \_/ \___|  |_||_____|
#  =======================================================
#   https://github.com/CiscoSteve42


from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
#from qtile_extras import widget
import os

mod = "mod4"
terminal = "alacritty"
os.environ["QT_QPA_PLATFORMTHEME"] = "qt6ct" 

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod], "f", lazy.spawn("librewolf")),
    Key([mod], "b", lazy.spawn("blueman-manager")),
    Key([mod, "control"], "v", lazy.spawn("virt-manager")),
    Key([mod], "a", lazy.spawn("alacritty -e yazi Books")),
    Key([mod], "c", lazy.spawn("kdeconnect-app")),
    Key([mod], "p", lazy.spawn("sxiv Pictures")),
    Key([mod], "w", lazy.spawn("wireshark")),
    Key([mod], "x", lazy.spawn("keepassxc")),
    Key([mod], "v", lazy.spawn("bash -c 'GTK_THEME=Dracula pavucontrol'")),
    Key([mod, "control"], "f", lazy.spawn("firefox")),
    Key([mod], "m", lazy.spawn("minecraft-launcher")),
    Key([mod, "control"], "m", lazy.spawn("curseforge")),
    Key([mod], "r", lazy.spawn("retroarch")),
    Key([mod, "control"], "d", lazy.spawn("discord"))


]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#bd93f9"], border_width=2,margin=2, border_focus='#50fa7b', border_normal='#ff79c6'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=18,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.GroupBox(font="Jetbrains Mono", active="#50fa7b", highlight_method="line", highlight_color="#bd93f9", inactive="#ff79c6", background="#6272a4"),
                widget.Prompt(font="Jetbrains Mono", foreground="#8be9fd", background="#6272a4", cursor_color="#50fa76"),
                widget.WindowName(font="Jetbrains Mono", background="#bd93f9", foreground="#50fa7b"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Cmus(font = "Jetbrains Mono", play_color="#50fa7b", noplay_color="#ff79c6", background="#6272a4"),
                widget.CheckUpdates(distro="Arch_paru", font="Jetbrains Mono", background="#8be9fd"),
                widget.CPU(font = "Jetbrains Mono", background="#ff79c6", foreground="#8be9fd"),
                widget.Net(font = "Jetbrains Mono", background="#50fa7b", foreground="ff79c6"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Clock(format="%m-%d-%Y %a %I:%M %p", background="#bd93f9", font = "Jetbrains Mono", foreground="#50fa7b"),
               # widget.QuickExit(),
		widget.WidgetBox(background="#6272a4", foreground="#8be9fd", font="Jetbrains Mono", widgets=[
		widget.Systray(background="#6272a4"),
        widget.BatteryIcon(background="6272a4"),
		]
		),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "CiscoSteve42"
