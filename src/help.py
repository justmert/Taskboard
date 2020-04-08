from render import colors
help_message = \
    f"""
   Tasks, boards, notes and snippets for the command-line environment

   {colors.BOLD}Usage{colors.END}  
      none             •    Display board view
      t  - task        •    Create a task
      n  - note        •    Create a note
      sn - snippet     •    Create a code snippet
      b  - begin       •    Start/pause task
      c  - check       •    Check/uncheck task
      e  - edit        •    Edit item description
      d  - delete      •    Delete an item
      f  - find        •    Search in item's descriptions
      s  - star        •    Star/unstart item
      p  - priority    •    Update priority of an item (*1, *2, *3)
      m  - move        •    Move item between boards
      l  - list        •    List notebooks with their items
      y  - copy        •    Copy an item description
      a  - archive     •    Display archived items
      r  - restore     •    Restore item from archive
      o  - oneline     •    Display items in one line
      v  - view        •    View code snippet's content
      at - attach      •    Attach an item to a notebook
      cc - copycon     •    Copy code snippet's content
      ec - editcon     •    Edit code snippet's content (in editor)
      fc - findcon     •    Search in code snippets' contents
      rf - refactor    •    Refactor items (resets their ids)
      cl - clear       •    Refactor and delete checked items, archive 
      tl - timeline    •    Display timeline view
      h -  help        •    Display help message
      ex - examples    •    Display helping examples
      exit             •    Just exit """

examples = \
    f"""
    It is easy actually, it follows like:
    {colors.BLUE}｢command name｣{colors.END} {colors.YELLOW}｢numbers if it needs｣{colors.END}{colors.GREEN2} ｢arguments as request or option｣{colors.END}

    {colors.BOLD}Examples{colors.END}
      These commands needs arguments:
      • {colors.BLUE}task{colors.END} Implement ai in my hello world program  
      • {colors.BLUE}note{colors.END} Php is bad 
      • {colors.BLUE}snippet{colors.END} Arch update mirror code {colors.GREEN2}@arch{colors.END}  
      • {colors.BLUE}begin{colors.END} {colors.YELLOW}1 2{colors.END}   
      • {colors.BLUE}check{colors.END} {colors.YELLOW}4 6 1{colors.END}
      • {colors.BLUE}edit{colors.END} {colors.YELLOW}2{colors.END} Resolve merge conflict
      • {colors.BLUE}delete{colors.END} {colors.YELLOW}2 6 7 4{colors.END}
      • {colors.BLUE}find{colors.END} git
      • {colors.BLUE}priority{colors.END} {colors.YELLOW}4 2{colors.END} {colors.GREEN2}*2{colors.END}
      • {colors.BLUE}move{colors.END} {colors.YELLOW}3{colors.END} {colors.GREEN2}fix{colors.END}
      • {colors.BLUE}copy{colors.END} {colors.YELLOW}7{colors.END}
      • {colors.BLUE}restore{colors.END} {colors.YELLOW}5 6{colors.END}
      • {colors.BLUE}view{colors.END} {colors.YELLOW}6{colors.END}
      • {colors.BLUE}attach{colors.END} {colors.YELLOW}3{colors.END} {colors.GREEN2}coding{colors.END}
      • {colors.BLUE}copycon{colors.END} {colors.YELLOW}5{colors.END}
      • {colors.BLUE}editcon{colors.END} {colors.YELLOW}3{colors.END}
      • {colors.BLUE}findcon{colors.END} {colors.YELLOW}10{colors.END} print
      Other commands doesn't need arguments so you can try easily"""
