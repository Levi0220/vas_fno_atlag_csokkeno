# vas_fno_atlag_csokkeno Package használata
## Leírás:
Ez a package 4 nodeból áll, egy Publisher-ből és 3 subsciber-ből.
## Működés:
A Publisher node "array_publisher" 8 db 50 és -50 közötti random számot publish-ol az "unsorted_array" topicra, amelyre a 3 subscriber pedig feliratkozik.
- "array_averager" átlagolja a kapott értékeket.
- "array_range" kiszámolja mekkora a tömb terjedelme (range).
- "array_sorter" csüökkenő sorrendbe helyezi a kapott értékeket.
## Használat:
- cd ros2_ws/src
- git clone https://github.com/Levi0220/vas_fno_atlag_csokkeno.git
- cd ~/ros2_ws
- colcon build --symlink-install
- source install/setup.bash     (Fontos!)
- ros2 launch vas_fno_atlag_csokkeno array.launch.py
