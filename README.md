# learning-kivy 
----------------------------------------
I will be updating this accordingly.
*Main Layouts:*
> GridLayout
> FloatLayout
> BoxLayout

*Main Objects:*
 > Button
 > Label
 > TextInput

*Layouts:*
> To create a layout inside another layout, new layout instance has to be created inside the layout block

Kivy Language:
> It facilitates writing code by providing a more user-friendly and less sophisticated syntax
# client_add_system-project
-----------------------------------------
I attempted to implement a system which simply adds person's name to a seperate file.
The features i want to implement are: Display, Remove and Edit previously added usernames. / Make the UI look more appealing. / Make it downloadable on mobile.
 Bugs I've encountered: add_client() function didn't work properly because of my silly mistake. I used super() to inherit properies from the client() function, which then appeared to be utterly useless as I couldn't find any usecase for it. The client() function was from my recentmini python project (26.12.2022 as I'm writing this).
 
  - 27/12/2022 -
I managed to implement display_users() function which as the name suggests displays users from users.txt.
Errors: Initially, the names were displayed on the screen, in the left bottom corner, which wasn't my intention. After I edited it, it completely stopped displaying the users. So I must work on that, and then learn UIX in kivy.

# Clicker Game
I started making this on NYE, but I ran into an error. The click() function which purpose is to display the number of clicks, didn't work. I asked ChatGBT about the Error I've ran into, and it gave it a suggesting that I perhaps should modify that function. 
