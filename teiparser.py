#!/usr/bin/env python

import xml.etree.ElementTree as ET


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
    root = ET.fromstring(TEST_STRING)    
    # strings = root.xpath('//text()')
    # result = list(root.iter())
    print(f"root length: {len(root)}")
    level = -1
    def print_child(elem, level):
        level += 1
        indent = " " * level
        print(f"{indent}{elem.tag}: {elem.text}")
        for child in elem:
            print_child(child, level)
    for child in root:
        print_child(child, level)

if __name__ == "__main__":
    parse()
