
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT CAPSTEXT GENERAL IEEE INDEX INTRO MONTH NUMBER REFERENCES YEARarticle : headerheader : code publication titleandauthor abstractheader : publication code titleandauthor abstractcode : YEARpublication : IEEE text MONTH YEARabstract : ABSTRACT text INDEXkeywords : INDEX text INTROtitleandauthor : texttext : GENERAL texttext : GENERAL'
    
_lr_action_items = {'INDEX':([10,15,20,],[-10,-9,21,]),'ABSTRACT':([10,11,12,13,15,],[-10,-8,16,16,-9,]),'MONTH':([9,10,15,],[14,-10,-9,]),'YEAR':([0,2,14,19,],[4,4,19,-5,]),'GENERAL':([4,6,7,8,10,16,19,],[-4,10,10,10,10,10,-5,]),'IEEE':([0,1,4,],[6,6,-4,]),'$end':([3,5,17,18,21,],[-1,0,-2,-3,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,2,],[1,8,]),'publication':([0,1,],[2,7,]),'text':([6,7,8,10,16,],[9,11,11,15,20,]),'abstract':([12,13,],[17,18,]),'titleandauthor':([7,8,],[12,13,]),'header':([0,],[3,]),'article':([0,],[5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> article","S'",1,None,None,None),
  ('article -> header','article',1,'p_article','parser.py',10),
  ('header -> code publication titleandauthor abstract','header',4,'p_header_code','parser.py',15),
  ('header -> publication code titleandauthor abstract','header',4,'p_header_pub','parser.py',19),
  ('code -> YEAR','code',1,'p_code','parser.py',23),
  ('publication -> IEEE text MONTH YEAR','publication',4,'p_publication','parser.py',27),
  ('abstract -> ABSTRACT text INDEX','abstract',3,'p_abstract','parser.py',31),
  ('keywords -> INDEX text INTRO','keywords',3,'p_keywords','parser.py',35),
  ('titleandauthor -> text','titleandauthor',1,'p_titleandauthor','parser.py',47),
  ('text -> GENERAL text','text',2,'p_text_general','parser.py',51),
  ('text -> GENERAL','text',1,'p_text','parser.py',55),
]