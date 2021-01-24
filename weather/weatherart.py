from styles import Style


def clear_sky():
    print("""{bold}{yellow}
       .   \\_,!,_/   ,
        `.,'     `.,'
         /         \\
      -- :         : --  
         \\         /
        ,'`._   _.'`.
       '   / `!` \\   `
    {end}""".format(bold=Style.BOLD, yellow=Style.YELLOW, end=Style.END))


def few_clouds():
    print("""{bold}
                        {yellow}\\   |   /{end}{bold}
              .-~~~-.     {yellow}_____{end}{bold}
      .- ~ ~-(       )_ _{yellow}/      \\ ~ ~{end}{bold}
     /                     ~ -. {yellow}|{end}{bold}
    |                           \\ {yellow} ~ {end}{bold}
        ~- . _____________ . -~
    {end}""".format(bold=Style.BOLD, end=Style.END, yellow=Style.YELLOW))


def scattered_clouds():
    print("""{bold}
              .-~~~-.
      .- ~ ~-(       )_ _
     /                     ~ -.
    |                           \\
     \\                         .'
       ~- . _____________ . -~
    {end}""".format(bold=Style.BOLD, end=Style.END))


def broken_clouds():
    print("""{bold}
              .-~~~-.{end}        -.{bold}
      .- ~ ~-(       )_ _{end}        )_ _{bold}   
     /                     ~ -.{end}        ~ -. {bold} 
    |                           \\{end}          \\{bold}
     \\                         .'{end}          .'{bold}
       ~- . _____________ . -~{end}  ______ . -~{bold}  
    {end}""".format(bold=Style.BOLD, end=Style.END))


def rain():
    print("""{bold}
              .-~~~-.
      .- ~ ~-(       )_ _
     /                     ~ -.
     \\                         .'
       ~- . _____________ . -~
       {blue}’   ’   ’   ’   ’   ’
      ’   ’   ’   ’   ’   ’
    {end}""".format(bold=Style.BOLD, blue=Style.BLUE, end=Style.END))


def thunderstorm():
    print("""{bold}
              .-~~~-.
      .- ~ ~-(       )_ _
     /                     ~ -.
     \\                         .'
       ~- . _____________ . -~
        {blue}’{end}{bold}   {yellow}/    /{end}{bold}   {blue}’   ’  
       ’{end}{bold}    {yellow}\\   \\{end}{bold}   {blue}’   ’
      ’{end}{bold}     {yellow}/  /{end}{bold}   {blue}’   ’{end}{bold}
            {yellow}\\ \\{end}
    """.format(bold=Style.BOLD, blue=Style.BLUE, yellow=Style.YELLOW, end=Style.END))


def snow():
    print("""{bold}
       .      .
       _\\/  \\/_
        _\\/\\/_
    _\\_\\_\\/\\/_/_/_
     / /_/\\/\\_\\ \\
        _/\\/\\_
        /\\  /\\
       '      '
    {end}""".format(bold=Style.BOLD, end=Style.END))


def mist():
    print("""{bold}
         ~~~~
      ~~~~~~~~~
           ~~~~~~~
      ~~~~~~~
        ~~~~~~~~~~~~~
    {end}""".format(bold=Style.BOLD, end=Style.END))
