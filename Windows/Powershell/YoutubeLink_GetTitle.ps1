<#
Title: Youtube link get title grabber.

You can just skip to # <Start> if you don't wana read anything

TOC:
Title | Description | What it should do | What you need to do | Notes | Future ideas | Disclaimer | The actual code

> Description:
If you are like me, and have over 5000 tabs stowed away and another 1000 being youtube urls which you cannot remember what they belong to, feel free to use this code.
Also because of the newer Youtube UI that appears in 2017 which makes highlighting a title a pain in the ass as it also highlights everything else below (i.e descriptions, comments, autoplay)
Uses abit of regex and powershell.

> What it should do:
Take the contents of a inputFile which should contain only Youtube URLs such as
https://www.youtube.com/watch?v=oIkhgagvrjI
https://youtu.be/oIkhgagvrjI?t=9m46s
https://www.youtube.com/watch?v=oIkhgagvrjI&index=6&list=PLzH6n4zXucko9k1NR7G-lz77eIwLNSU9s

and write to a outputFile something like the following: video | Title
https://www.youtube.com/watch?v=oIkhgagvrjI | Why do YouTube views freeze at 301?
https://youtu.be/oIkhgagvrjI?t=9m46s | Why do YouTube views freeze at 301?
https://www.youtube.com/watch?v=oIkhgagvrjI&index=6&list=PLzH6n4zXucko9k1NR7G-lz77eIwLNSU9s | Why do YouTube views freeze at 301?

> What you need to do:
Change the input and output file section.

> Notes:
1) If the YouTube video no longer exists it may return something like <URL LINK> | <blank>
2) I actually don't know why this works but hay.
3) I won't go into the specifics on why, what, why you should, why you shouldn't, but you generally cannot run a ps1 script because of Windows PowerShell execution policies. But I use ISE to run sections so....
4) I can run this on Powershell 5.0 (I think this is the version I am using)

> Future ideas:
I didn't change the protective url encoding like &#39; or &quot; so you will see it in your text.

> Disclaimer:
! Reminder: Always read and try to understand whatever code you get from the internet before running it on your machine. !
This place may not always be updated.
The code does clear the inputFile and outputFile
#>

#The actual code
# ! Reminder: Always read and try to understand whatever code you get from the internet before running it on your machine. !
# <Start>

#!Requires your input: Change inputFile and outputFile to fit your uses
$inputFile="c:\url.txt"
$outputFile="c:\output.txt"

#Sample items, might have more idk
$toMatch=@("&#39;","&#34;","&#60;","&#62;","&quot;","&amp;","&lt;","&gt;")
$toReplaceWith=@("'",'"',"<",">",'"',"&","<",">")

clear-content -path $outputFile
get-content $inputFile | ForEach-Object{
    $uri=$_;
    $title=$($(invoke-restmethod -uri $uri).toString() -split '\n' | Select-String -Pattern "(?<=<title>)(.*)(?= - Youtube<\/title>)").matches.value
    
    For ($i=0; $i -lt $toMatch.Length; $i++){ #Not the most efficient method.
        $title=$title.Replace($toMatch[$i],$toReplaceWith[$i])   
    }
    
    echo "$uri | $title " | Out-File $outputFile -append
}
clear-content -path $inputFile
# <End>
