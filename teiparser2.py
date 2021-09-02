#!/usr/bin/env python

from bs4 import BeautifulSoup as BS
from bs4 import Tag
# from bs4 import NavigableString, Tag

TEST_STRING = '''
<div1 id="crossta_be^fa^ci^o" orig_id="n47320" key="ta_be^fa^ci^o" opt="n"><head extent="full" lang="la" opt="n" orth_orig="tābĕfăcĭo">tabefacio</head>, <itype opt="n">fēci, 3</itype>, <pos opt="n">v. a.</pos> <etym opt="n">tabes-facio</etym>, <sense id="n47320.0" n="I" level="1" opt="n"><i>to melt</i>, <i>dissolve.</i>—<usg type="style" opt="n">Trop.</usg>: <cit><quote lang="la">tabefac audaciam virtutis eorum,</quote> <bibl n="Perseus:abo:tlg,0527,023:4:32"><author>Vulg.</author> 1 Macc. 4, 32</bibl></cit>: <cit><quote lang="la">vigilia honestatis tabefaciet carnes,</quote> <i><i>subdue</i>,</i> <bibl default="NO"><author>id.</author> Ecclus. 31, 1</bibl></cit>.—Hence, <mood opt="n">Part.</mood>: <orth extent="full" lang="la" opt="n">tābē̆factus</orth>, <itype opt="n">a, um</itype>, <i>melted</i>, <i>dissolved</i> (post-class.): <cit><quote lang="la">tabefactis nivibus,</quote> <bibl default="NO"><author>Sol.</author> 2 <i>med.</i></bibl></cit>: <cit><quote lang="la">cadaver in suo sanguine,</quote> <bibl n="Perseus:abo:tlg,0031,026:14:14"><author>Vulg.</author> Jud. 14, 14</bibl></cit>.</sense></div1>
'''

TEST_STRING_Formatted = '''
<div1 id="crossta_be^fa^ci^o" orig_id="n47320" key="ta_be^fa^ci^o" opt="n">
   <head extent="full" lang="la" opt="n" orth_orig="tābĕfăcĭo">tabefacio</head>
   ,
   <itype opt="n">fēci, 3</itype>
   ,
   <pos opt="n">v. a.</pos>
   <etym opt="n">tabes-facio</etym>
   ,
   <sense id="n47320.0" n="I" level="1" opt="n">
      <i>to melt</i>
      ,
      <i>dissolve.</i>
      —
      <usg type="style" opt="n">Trop.</usg>
      :
      <cit>
         <quote lang="la">tabefac audaciam virtutis eorum,</quote>
         <bibl n="Perseus:abo:tlg,0527,023:4:32">
            <author>Vulg.</author>
            1 Macc. 4, 32
         </bibl>
      </cit>
      :
      <cit>
         <quote lang="la">vigilia honestatis tabefaciet carnes,</quote>
         <i>
            <i>subdue</i>
            ,
         </i>
         <bibl default="NO">
            <author>id.</author>
            Ecclus. 31, 1
         </bibl>
      </cit>
      .—Hence,
      <mood opt="n">Part.</mood>
      :
      <orth extent="full" lang="la" opt="n">tābē̆factus</orth>
      ,
      <itype opt="n">a, um</itype>
      ,
      <i>melted</i>
      ,
      <i>dissolved</i>
      (post-class.):
      <cit>
         <quote lang="la">tabefactis nivibus,</quote>
         <bibl default="NO">
            <author>Sol.</author>
            2
            <i>med.</i>
         </bibl>
      </cit>
      :
      <cit>
         <quote lang="la">cadaver in suo sanguine,</quote>
         <bibl n="Perseus:abo:tlg,0031,026:14:14">
            <author>Vulg.</author>
            Jud. 14, 14
         </bibl>
      </cit>
      .
   </sense>
</div1>
'''


def parse():
    soup = BS(TEST_STRING, 'html.parser')
    div1 = soup.div1
    head = soup.head
    print("~~~~~~~~~~~~~~~~~")
    print(head.getText())
    global count
    count = 1
    for child in div1.children:
        print_element(child)


def print_element(elem, level=-1):
    level += 1
    indent = "  " * level
    if isinstance(elem, Tag):
        if len(elem.contents) == 1:
            if elem.name == 'i':
                # import pdb; pdb.set_trace()
                global count
                print(f"# Sense {count}:")
                print(f"{elem.string}")
                count += 1
            else:
                print(f"{indent}{elem.name}: {elem.string}")
        elif elem.name == 'cit':
            print(f"{indent}{elem.name}: {elem.getText()}")
        else:
            print(f"{indent}{elem.name}")
            for child in elem:
                print_element(child, level)


if __name__ == "__main__":
    parse()
