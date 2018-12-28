map_test = [
'/->-\\',
'|   |  /----\\',
'| /-+--+-\\  |',
'| | |  | v  |',
'\\-+-/  \\-+--/',
'  \\------/',
        ]

map_test_part2 = [
'/>-<\\  ',
'|   |  ',
'| /<+-\\',
'| | | v',
'\\>+</ |',
'  |   ^',
'  \\<->/'
]


map = [
'              /----------------------\                                                                              /--------------------------\      ',
'              |                     /+------------------------------------------------------------------------------+-------------\            |      ',
'              |                  /--++--------------------------------------------------------\                     |             |            |      ',
'              |                  | /++--------------------------------------------------------+---------------------+-------\     |            |      ',
'              | /----------------+-+++--------\ /---------------------------------------------+---------------------+\      |     |            |      ',
'              | |                | |||        | |                                            /+---------------------++------+-----+-----------\|      ',
'         /----+-+-\              | |||        | |               /----------------------------++---------------------++---\  |     |           ||      ',
'         |    | | |/-------------+-+++--------+-+---------------+--->------------------------++--\     /------------++---+--+-----+---------\ ||      ',
'         |    | | ||     /-------+-+++--------+-+---------------+----------------------------++--+-----+-----\      ||   |  |     |         | ||      ',
'        /+----+-+-++-----+-------+-+++--------+-+---------------+----------------------------++--+--\  |     |      ||   |  |     |         | ||      ',
'        ||    |/+-++-----+-------+-+++--------+-+---------------+----------------------------++--+--+--+-----+-\    ||   |  |     |         | ||      ',
'  /-----++----+++\||     |       | |||        | |               |                            ||  |  |  |     | |    ||   |  |  /--+---------+-++----\ ',
'  |     ||    ||||||     |       | |||        | |            /--+----------------------------++--+--+--+-----+-+----++---+--+--+--+------\  | ||    | ',
'  |     ||    ||||||     |       | |||        | |   /--------+\ |      /---------------------++--+--+--+-----+-+----++---+--+--+--+------+--+-++---\| ',
'  |     ||    ||||||/----+-------+-+++--------+-+---+--------++-+------+---------------------++--+--+--+-----+-+----++---+\ |  |  |      |  | ||   || ',
'  |     ||    |||||||/---+-------+-+++--------+-+---+--------++-+------+----------------\    ||  |  |  |     | |    ||   || |  |  |      |  | ||   || ',
'  |     ||    ||||||||   |       | |||        | |   |        || |      |                |    ||  |  |  |     | |  /-++---++-+--+--+------+--+-++-\ || ',
'  |  /--++----++++++++---+-------+-+++--\   /-+-+---+--------++-+------+----------------+----++--+--+\ |     | |  | ||   || |  |  |      |  | || | || ',
' /+--+--++----++++++++---+-------+-+++--+---+-+-+---+--------++-+------+----------------+-\  ||  |  || |     | |  | ||   || |  |  |      |  | || | || ',
' ||  |  ||    ||||||||   |       | |||  |   | | |   |        || |      |                | |  ||/-+--++-+-----+-+--+-++\  || |  |  |      |  | || | || ',
' ||  |  ||    ||||||||   |       | |||  |   | | |   |        || |      |       /--------+-+--+++-+--++\|     | |  | |||  || |  |  |      |  | || | || ',
' ||  |  ||    ||||||||   |       | |||  |   | | |   |        || |      |       |        | |  ||| |  ||||     | |  | |||  || |  |  |      |  | || | || ',
' ||  |  ||    |||||^||   \-------+-+++--+---+-+-+---+--------++-+------+-------+--------+-+--+++-+--++++-----/ |  | |||  || |  |  |      |  | || | || ',
' ||  |  \+-<--++++++++-----------+-+++--+---+-+-+---+--------++-+------+-------+--------+-+--+++-+--/|||       |  | |||  || |  |  |      |  | || | || ',
' ||  |   |    ||||||||      /----+-+++--+---+-+-+---+--------++-+----\ |       |        | |  ||| |   |||/------+--+-+++--++-+--+--+------+--+\|| | || ',
' ||  |   |    ||||||||      |    | |||/-+---+-+-+---+--------++-+----+-+-------+--------+-+--+++-+---++++------+--+-+++--++-+--+--+------+-\|||| | || ',
' ||  |   |    ||||||||      |    | |||| |  /+-+-+---+--------++-+----+-+-------+--------+-+--+++-+---++++------+--+-+++--++-+--+--+--\   | ||||| | || ',
' ||  |   |    ||||||||      |    | \+++-+--++-+-+---+--------++-+----+-+-------+--------+-+--+++-+---++++------+--+-+++--++-/  |  |  |   | ||||| | || ',
' ||  |   |    ||||||||      |    |  ||| |/-++-+-+---+--------++-+----+\|       |        | |  ||| |   ||||      |  | |||  ||    |  |  |   | ||||| | || ',
' ||  |/--+----++++++++---->-+----+--+++-++-++-+-+---+--------++-+---\|||       |        | |  ||| |   ||||      |/-+-+++--++----+--+\ |   | ||||| | || ',
' ||  ||  |    ||||||||     /+----+--+++-++-++-+-+---+--------++-+---++++-------+--------+-+--+++-+---++++------++-+-+++--++---\|  || |   | ||||| | || ',
' ||  ||  |    ||||||||     ||    | /+++-++-++\| |   |        || ^   ||||       |        | |  ||| |   ||||/-----++-+-+++--++---++--++-+---+\||||| | || ',
' ||  ||  |/---++++++++-----++----+-++++-++-++++-+---+--------++-+---++++-------+--------+-+--+++-+\/-+++++-----++-+-+++--++---++\ || |   ||||||| | || ',
' ||  ||  ||   ||||||||     ||    | |||| || |||| |   |        || |   ||||       |        | |  ||| ||| |||||     || | |||  ||   ||| || |   ||||||| | || ',
' ||  ||  ||   ||||||||     ||    | |||| || ||||/+---+--------++-+---++++-------+--------+-+\ ||| ||| |||||     || | |||  ||   ||| || |   ||||||| | || ',
' ||  || /++---++++++++-----++----+-++++-++-++++++---+--------++-+---++++-------+--------+-++-+++-+++-+++++\    || | |||  ||   ||| || |   ||||||| | || ',
' ||  || |||   ||||||||     ||    |/++++-++-++++++---+--------++\|   ||||       |        |/++-+++-+++-++++++--\ || | |||  ||   ||| || |   ||||||| | || ',
' ||  || |||   ||||||||     ||    |||||| || ||||||   |        ||||   ||||       \--------++++-+++-+++-+/||||  | || | |||  ||   ||| || |   ||||||| | || ',
' |\--++-+++---+++/||||     ||    |||||| || ||||||   |        ||||   |||| /--------------++++-+++-+++-+-++++--+-++-+-+++--++---+++-++-+\  ||||||| | || ',
' |   \+-+++---+++-++++-----++----++++++-/| ||||||   |        ||||   |||| |              |||| ||| ||| | ||||  | || | |||  ||   ||| || ||  ||||||| | || ',
' |    | |||   ||| ||||     ||    |||||| /+-++++++---+--------++++---++++-+--------------++++-+++-+++-+-++++--+\|| | |||  ||   ||| || ||  ||||||| | || ',
' |    | |||   |\+-++++-----++----++++++-++-++++++---+--------++++---++++-+--------------++++-+++-+++-+-++++--++/| | |||  ||   ||| || ||  ||||||| | || ',
' |    | |||   | | ||||     ||/---++++++-++-++++++---+--------++++---++++-+------------\ |||| ||| ||| | ||\+--++-+-+-+++--++---+++-++-++--+/||||| | || ',
' |    | |||   | | ||||     |||   |||||| || ||||||   | /------++++---++++-+------------+-++++-+++-+++-+-++-+--++-+-+-+++--++--\||| || ||  | ||||| | || ',
'/+----+-+++---+\| ||||     |||   |||||| || ||||||   | |      ||||   |||| |            | |||| ||| ||| | |\-+--++-+-+-+++--++--++++-++-++--+-++/|| | || ',
'||    | |||   ||| ||||     |||   |||||| || ||||||   \-+------+/|\---++++-+------------+-++++-+++-+++-+-+--+--++-+-+-+++--/|  |||| || ||  | || || | || ',
'||  /-+-+++---+++-++++-\   |||   |||||| |\-++++++-----+------+-+----++/| |       /----+-++++-+++-+++-+-+--+--++-+-+\|||   |  |||| || ||  | || || | || ',
'||  | | |||   ||| |||| |   |||   |||||| |  ||||\+-----+------+-+----++-+-+-------+----+-+++/ ||| ||| | |/-+--++-+-+++++--\|  |||| || ||  | || || | || ',
'||  | | |||   ||| |||| |   |||   |||||| |  |||| |     |      | |    || | |       |    | |||  ||| ||| | || |  || | |||||  ||  |||| || ||  | || || | || ',
'||  |/+-+++---+++-++++-+---+++---++++++-+--++++-+-----+------+-+----++-+-+-------+---\| |||  ||\-+++-+-++-+--++-+-++++/  ||  |||| || ||  | || || | || ',
'||  ||| ||\---+++-++++-+---+++---++++++-+--++++-+-----+------+-+----++-+-+-------+---++-+++--++--+/| | \+-+--++-+-++++---++--++++-++-++--+-+/ || | || ',
'||  ||| ||/---+++-++++-+---+++---++++++-+--++++-+-----+------+-+----++-+-+-----<-+---++-+++--++-\| | |  | |  || | ||\+---++--++++-++-++--+-+--+/ | || ',
'||  ||| |||   ||| |||| |   |||   |||||| |  |||| |     |      | |    || | |       |   || |||  ||/++-+-+--+-+--++-+-++-+---++\ |||| || ||  | |  |  | || ',
'||  ||| |||   \++-++++-+---+++---++++/| |  ||||/+-<---+------+-+----++-+-+-------+---++-+++--+++++-+\|  | |  || | || |   ||| |||| || ||  | |  |  | || ',
'||  ||| |||    || |||| |   |||   |||| | |  ||||||     |      | |  /-++-+-+-------+---++-+++--+++++-+++--+-+-\|| | || |   ||| |||| || ||  | |  |  | || ',
'||  ||| |||    || |||| |   |||   |||| | |  ||||||     |      | |  | || | |       |   || |\+--+++++-+++--+-+-+/|/+-++-+---+++-++++-++-++--+-+\ |  | || ',
'||  ||| |||    || |||| |   |||   |||| | |  ||||||     |      | |  | || | |       ^   || | |  ||||| |||  | | | ||| || |   ||| |||| || ||  | || |  | || ',
'||  ||| |||    || |||| |   |||   |||| | |  ||||||  /--+------+-+--+-++-+-+-------+---++-+-+--+++++-+++--+-+-+-+++-++-+---+++-++++-++-++\ | || |  | || ',
'||  ||| |||    || |||| |   |||   |||| | |  ||||||  |  |      | |  | || | |       \---++-+-+--+++++-+++--+-+-+-+++-+/ |   ||| |||| || ||| | || |  | || ',
'|\--+++-+++----++-++++-+---+++---++++-+-+--++++++--+--+------+-+--+-++-+-+-----------++-+-/  ||||| |||  | | | ||| |  |   ||| |||| || ||| | || |  | || ',
'|   ||| |||    || |||| |   |||   |||| | |  ||||||  | /+------+\|  | || | |           || |    ||||| |||  | | | ||| |  |   ||| |||| || ||| | || |  | || ',
'|   ||| |||    || |||| |   |||   |||| | |  ||||||  | ||      |||  | || | |/----------++-+----+++++-+++--+-+-+-+++-+--+---+++-++++-++\||| | || |  | || ',
'|   ||\-+++----++-++++-+---+++---++++-+-+--++++++--+-++------+++--+-/| | ||          || |    ||||| |||  | | | |||/+--+---+++-++++-++++++-+-++-+--+\|| ',
'|/--++--+++----++-++++-+\  |||   |||| | |/-++++++--+-++------+++--+--+-+-++----------++-+----+++++-+++--+-+-+-+++++--+---+++-++++<++++++-+-++-+\ |||| ',
'||  ||  |||  /-++-++++-++--+++---++++-+-++-++++++--+-++------+++--+--+-+-++----------++-+----+++++-+++--+-+-+-+++++--+\  ||| |||| |||||| | || || |||| ',
'||  ||  |||  | || ||||/++--+++---++++-+-++-++++++--+-++------+++--+--+-+-++----------++-+----+++++-+++--+-+-+\|||||  ||  ||| |||| |||||| | || || |||| ',
'||/-++--+++--+-++-+++++++--+++---++++-+\|| |||||\--+-++------+++--+--+-+-++----------++-+----+++++-+++--+-+-+++++++--/|  ||| |||| |||||| | || || |||| ',
'||| ||  |||  | || |||||||  |||   |||| |||| ||||| /-+-++------+++--+--+-+-++--------\ || |    ||||| |||  | | |||||||  /+--+++-++++-++++++-+-++-++\|||| ',
'||| ||  |||  | || |||||||  |||   |||| |||| ||||| | | ||      |||  |  | | ||        | || |    ||||| |||  | | |||||||  ||  ||| |||| |||||| | || ||||||| ',
'||| ||  |||  | || |||||||  |\+---++++-++++-+++++-+-+-++------+++--+--/ | ||    /---+-++-+----+++++-+++--+-+-+++++++--++--+++-++++\|||||| | || ||||||| ',
'||| ||  |||  | || ||\++++--+-+---++++-++++-+++++-+-+-++------+++--+----+-++----+---+-++-+----+++++-+++--+-+-+++++++--++--+/| ||||||||||| | || ||||||| ',
'||| ||  |||  | || || ||||  | |   |||| |||| \++++-+-+-++------+++--+----+-++----+---+-++-+----+++++-+++--+-+-+++++++--++--+-+-++++++++/|| | || ||||||| ',
'||| ||  |||  | || || |v||  | |  /++++-++++--++++-+-+-++------+++--+----+-++-\  |   | || |    ||||| |||  | | |||||||  ||  | | |||||||| || | || ||||||| ',
'||v || /+++--+-++-++-++++--+-+--+++++-++++--++++-+-+-++------+++--+----+-++-+--+---+-++-+----+++++-+++--+-+\|||||||  ||  | | |||||||| || | || ||||||| ',
'||| || ||||  | || || ||||  | |  ||||| ||||  |||| | | ||      |||  |/---+-++-+-\|   | || |    ||||| |||  | |||||||||  ||  | | |||||||| || | || ||||||| ',
'||| || ||||  | || || ||||  | |  ||||| ||||  |||| | | ||      |||  ||   | || | ||/--+-++-+----+++++-+++--+-+++++++++\ ||  | | |||||||| || | || ||||||| ',
'||| || ||||  | || || ||||  | |  |||\+-++++--+/|| | | ||      |||  ||   \-++-+-+++--+-++-+----+++++-+++--+-++++++++++-++--+-+-++++++++-++-+-++-+++++/| ',
'||| || ||||  | || || ||||  | |  ||| | ||||  | || | | ||      |||  ||     || | |||  | || |    ||||| |||  | |||||||||| \+--+-+-++++++++-++-+-++-++/|| | ',
'||| || ||||  \-++-++-++++--+-+--+++-+-++++--+-++-+-+-++------+++--++-----++-+-+++--+-++-+----+++++-+++--+-++++++++++--/  | | ||\+++++-++-+-++-++-++-/ ',
'||| || ||||    || || ||||  | |  ||| | \+++--+-++-+-+-++------+++--++-----++-+-+++--+-++-+----+++++-+++--+-++++++++++-----+-+-++-+++++-++-+-/| || ||   ',
'||| || ||||    ||/++-++++--+-+--+++-+--+++--+-++-+-+-++------+++--++-----++-+-+++--+-++-+----+++++-+++--+-++++++++++-----+-+\|| ||||| || |  | || ||   ',
'||| || |||\----+++++-++++--+-+--+++-+--+++--+-++-+-+-++------+++--++-----++-+-+++--+-++-+----+++/| |||  | ||||||||||     | |||| ||||| || |  | || ||   ',
'||| || |||     ||||| ||||  | |  ||| |  |||  | || | | ||      |||  ||     || | |||  | || |    ||| | |||  \-++++++++++-----/ |||| ||||| || |  | || ||   ',
'|\+-++-+++-----+++++-+++/  | |  ||| |  ||\--+-++-+-+-++------+++--++-----++-+-+++--+-++-+----+++-+-+++----++++++++++-------++++-+++++-++-+--+-+/ ||   ',
'| | || |||     ||||| |||   | |  ||| |  ||   | || | | ||      |||  ||     || | |||/-+-++-+----+++-+-+++----++++++++++-------++++-+++++-++-+\ | |  ||   ',
'| | || |||     ||||| ||| /-+-+--+++-+--++\  | || | | || /----+++--++-----++-+-++++-+-++-+----+++-+-+++----++++++++++-------++++-+++++-++-++-+-+--++-\ ',
'| | || |||     ||||| ||| | | |  ||| |  |||  | || | | || |    |||  ||     || | |||| | || |    \++-+-+++----++++++++++-------++++-+++++-++-++-+-/  || | ',
'| | || ||\-----+++/| ||| | | |  ||| |  |||  | || | | || |    |||  ||     || | |||| | || |     |\-+-+++----++++++++++-------/||| ||||| || || |    || | ',
'| | || ||  /---+++-+-+++-+-+-+--+++-+--+++--+-++-+-+-++-+----+++--++-----++-+-++++-+-++-+-----+--+-+++----++++++++++--\     ||| ||||| || || |    || | ',
'\-+-++-++--+---/|| | ||| | | |  ||| |  |||  | || | | || |    |||  ||     || | |||| | || |     |  | \++----++++++++++--+-----+++-/|||| || || |    || | ',
'  | || ||  |    || | ||| | | |  ||| |  |||  | || | | || |    |||  ||     || | |||| | || |     |  |  ||    ||||||||||  |     |||  |||| || || |    || | ',
'  | || ||  |    \+-+-+++-+-+-+--+++-+--+++--+-/| | | || |    |||  ||     || | |||| | || |     |  |  ||/---++++++++++--+-----+++--++++-++-++-+\   || | ',
'  | || || /+-----+-+-+++-+-+-+--+++-+--+++--+--+-+-+-++-+----+++-\||     || | |||| | || |     |  |  |||   ||||||||||  |     |||  ||^| || || ||   || | ',
'  | || || ||     | | ||| | | |  ||| |  |||  |  | | | || |    ||| |||     || | |||| | || |     |  |  |||   ||||||||||  |     |||  |||| || || ||   || | ',
'  | || || ||     | | ||| | | |  ||| |  |||  |  | | | || |    ||| |||     || | ||||/+-++-+-----+--+-\|||   ||||||||||  |     |||  |||| || || ||   || | ',
'/-+-++-++-++-----+-+-+++-+-+-+--+++-+--+++--+--+-+-+-++\|    ||| |||     || | |||\++-++-+-----+--+-++++---++++++++++--+-----+++--++++-++-+/ ||   || | ',
'| | ||/++-++-----+-+-+++-+-+-+--+++-+--+++--+--+-+-+-++++----+++-+++\    || | ||| || || |     |  | ||||   ||||||||||  |     |||  |||| || |  ||   || | ',
'| | ||||| ||     | | ||| | |/+--+++-+--+++--+--+-+-+-++++----+++-++++----++-+-+++-++-++-+-----+--+-++++---++++++++++--+-----+++-\|||| || |  ||   || | ',
'| | |||||/++-----+-+-+++\| |||  ||| \--+++--+--+-+-+-++++----+++-++++----++-+-+++-++-++-+-----+--+-++++---++++++++++--+-----+++-++/|| || |  ||   || | ',
'| | ||||||||     | | ||||| |||  |\+----+++--+--+-+-+-++++----+++-++++----++-+-+++-++-++-+-----/  | ||||   ||||||||\+--+-----+++-++-++-++-+--++---/| | ',
'| | ||||||||     | | ||||| |||  | |    |||  |  | | | ||||    ||| ||||    || | ||| || || |        | ||||   |||||||| |  |     ||| || || || |  ||    | | ',
'| | ||||||||     | | ||||| |||  | |    |||  |  | | | ||||    \++-++++--->++-+-+++-++-++-+--------+-++++---++++++++-+--+-----+++-++-++-++-/  ||    | | ',
'| | ||||||||     | | ||||| |||  | |  /-+++--+--+-+-+-++++-----++-++++\   || | ||| || || |        | ||||   |||||||| |  |     ||| || || ||    ||    | | ',
'| | ||||||||     | | ||||| |||  | |  | |||  |  | | | ||||     || |||||   || | ||| || || |        | ||||   |||||||| |  |     ||| || || ||    ||    | | ',
'| | ||||||||     | | ||||| |||  \-+--+-+++--+--+-+-+-++++-----++-+++++>--++-/ ||| || || |        | ||||   |||||||| |  |     ||| || || ||    ||    | | ',
'| | ||||||||     | | ||||| |||   /+--+-+++--+--+\| | ||||     || |||||   ||   ||| || || |        | |||\---++++++++-+--+-----+++-++-++-++----+/    | | ',
'| \-++++++++-----+-+-+++++-+++---++--+-/||  |  ||| | ||||     || |||||  /++---+++-++-++-+--------+\|||    |||||||| |  |     ||| || || ||    |     | | ',
'|   ||||||||     | | ||||| |||   ||  |  ||  |  \++-+-++++-----++-+++++--+++---+++-++-++-+--------+++/|    |||||||| |  |     ||| || || ||    |     | | ',
'|   ||||||\+-----+-+-+++++-+++---++--+--++--+---++-+-++++-----++-/||||  |||   ||| || ||/+--------+++-+----++++++++-+--+-----+++-++-++-++----+\    | | ',
'|   |||||| |     | \-+++++-+++---++--+--++--+---++-+-++++-----++--++++--+++---+++-++-++++--------/|| |    ||||||\+-+--+-----+++-++-/|/++----++\   | | ',
'|   |||||| |     |   ||||| |||   ||  |  \+--+---++-+-++++-----++--++++--+++---+++-++-++++---------++-+----++++/| | |  |     ||| ||  ||||    |||   | | ',
'|   |||||| |     |   ||||| |||   ||  |   |  |   || | ||||     ||  ||||  |\+---+++-++-++++---------++-+----++++-+-+-+--+-----+++-++--++/|    |||   | | ',
'|   |||||| |    /+---+++++-+++---++--+---+--+---++-+-++++-----++--++++--+-+---+++-++-++++---------++-+----++++-+-+-+--+\    ||| ||  || |    |||   | | ',
'|   |||||\-+----++---+++/| |||   ||  |   |  |   || | ||||     ||  ||||  | |   ||| || ||||         || |    |||| | | |  ||    ||| ||  || |    |||   | | ',
'|   |||||  |  /-++---+++-+-+++---++--+---+--+---++-+-++++-----++--++++-\| \---+++-++-++++---------++-+----++++-+-+-+--++----+++-++--/| |    |||   | | ',
'|   |||||  |  | ||   ||| | ||\---++--+---+--+---++-+-++++-----++--++++-++-----+++-++-+/||         || |  /-++++-+-+-+--++----+++-++---+-+----+++-\ | | ',
'|   |||||  |  | ||   ||| | ||    \+--+---+--+---/| | ||||     ||  |||| ||     ||| || | ||         || |  | |||| | | |  ||   /+++-++---+-+----+++-+-+\| ',
'|   |||||  |  | ||   ||| | ||     |  |   |  |    | | ||||     ||  |||| ||     ||| \+-+-++---------+/ |  | |||| | | |  ||   |||| ||   | |    ||| | ||| ',
'|   |||||  |  | ||   ||| | |\-----+--+---+--+----+-+-++++-----++--++++-++-----+++--+-+-++---------+--+--+-++++-+-+-+--++---++++-/|   | |    ||| | ||| ',
'|   |||||  |  | ||   ||| | \------+--+---+--+----+-+-++++-----++--++++-++-----+++--+-+-++---------+--+--+-++++-+-+-+--++---+++/  |   | |    ||| | ||| ',
'|   |||||  |  | ||   \++-+--------+--+---+--+----+-+-++++-----++--++++-++-----+++--+-+-+/         |  |  | |||| |/+-+--++---+++---+--\| |    ||| | ||| ',
'\---+++++--+--+-++----++-+--------+--+---+--+----+-+-++/|     ||  |||| ||     |||  | | |          |  |  | |||| ||| |  ||   |||   |  || |    ||| | ||| ',
'    |||||  |  | ||    || \--------+--+---/  |    | | || |     ||  |||| ||     |||  | | \----------+--+--+-++++-+++-+--++---+++---+--++-+----+/| | ||| ',
'    |||||  |  | || /--++----------+--+--\   |    | \-++-+-----++--++++-++-----+++--+-+------------+--+--+-++++-+++-+--++---+++---+--++-/    | | | ||| ',
'    |||||  |  | || |  ||          |  |  |   \----+---++-+-----++--++++-++-----+++--+-+------------+--/  | |||| ||| |  ||   |||   |  ||      | | | ||| ',
'    |||||  |  | || |  ||          |  |  |        |   |\-+-----++--++++-++-----+++--+-+------------+-----+-++++-+++-+--++---++/   |  ||      | | | ||| ',
'    |||||  \--+-++-+--++----------+--+--+--------+---+--+-----++--++++-++-----+++--+-+------------+-----+-++++-+++-+--/|   ||    |  ||      | | | ||| ',
'    |\+++-----+-++-+--++----------+--+--+--------+---+--+-----++--++++-++-----+++--+-/            |     | |||| ||| |   |   ||    |  ||      | | | ||| ',
'    | |||  /--+-++-+--++----------+--+--+--------+---+--+-----++--++++-++-----+++\ |              |     | |||| ||| |   |   ||    |  ||      | | | ||| ',
'    | |||  |  | || |  ||          |  |  |        |   |  \-----++--++++-++-----++++-+--------------+-----+-++++-+++-+---+---++----+--++------+-+-+-++/ ',
'    | |||  |  | || |/-++----------+--+--+--------+---+----\   ||  |||| ||     |||| |              |     | |||| ||| |   |   ||    v  ||      | | | ||  ',
'    | |||  |  | || || ||          |  |  |        \---+----+---++--++++-++-----++++-/              |     | |||| ||| |   |   ||    |  ||      | | | ||  ',
' /--+-+++--+-\| || || ||          |  |  |            |    |   ||  |||| ||     ||||                |     | |||| ||| |   |   ||    |  ||      | | | ||  ',
' |  | |||  | || || \+-++----------+->+--/            |    |   ||  |\++-++-----/|||                |     | |||| ||| |   |   ||    |  ||      | | | ||  ',
' |  | |||  | || ||  | ||          |  |               |    |   ||  | || ||      |||               /+-----+-++++-+++-+---+---++----+--++------+-+-+-++\ ',
' |  | ||\--+-++-++--+-++--->------+--+---------------+----+---++--+-++-++------+++---------------++-----+-/||| ||| |   |   ||    |  ||      | | | ||| ',
' |  | ||   | || ||  | ||          \--+---------------+----+---+/  | || ||      |||               ||     |  ||| |\+-+---+---++----+--/|      | | | ||| ',
' |  | ||   | || ||  | \+-------------+---------------+----+---+---+-++-++------+++---------------++-----+--++/ | | |   |   ||    |   |      | | | ||| ',
' |  | ||   | |\-++--+--+-------------+---------------+----+---+---+-++-/|      |\+---------------++-----+--++--+-+-/   |   ||    |   \------+-/ | ||| ',
' |  | ||   | |  ||  |  |             |               |    |   |   | ||  \------+-+---------------+/     |  ||  | |     |   ||    |          |   | ||| ',
' |  \-++---+-+--++--+--/             \---------------+----+---+---+-+/         | |               |      \--++--+-+-----+---++----+----------+---/ ||| ',
' |    |\---+-+--++--+--------------------------------+----+---+---+-+----------+-+---------------+---------/|  | \-----+---++----+----------+-----/|| ',
' \----+----+-/  ||  |                                \----+---/   | |          | |               |          |  |       |   ||    |          |      || ',
'      |    |    ||  |                                     |       \-+----------+-+---------------+----------/  |       |   ||    |          |      || ',
'      |    |    \+--+-------------------------------------+---------+----------+-+---------------+-------------+-------/   \+----+----------+------/| ',
'      |    |     \--+-------------------------------------+---------+----------+-+---------------+-------------+------------/    |          |       | ',
'      |    \--------+-------------------------------------+---------+----------+-/               |             |                 |          |       | ',
'      |             \-------------------------------------/         |          \-----------------+-------------+-----------------/          |       | ',
'      |                                                             |                            |             \----------------------------/       | ',
'      \-------------------------------------------------------------/                            \--------------------------------------------------/ ',
]