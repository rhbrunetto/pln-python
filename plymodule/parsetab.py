
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT CHAPTER_MARK GENERAL IEEE INDEX MONTH NUMBER REFERENCES REFERENCE_B REFERENCE_L TERMS YEARarticle : header content referencesheader : code publication titleandauthor abstract keywordsheader : publication code titleandauthor abstract keywordscode : YEARcode : NUMBERpublication : IEEE text MONTH YEARabstract : ABSTRACT text INDEXkeywords : text TERMS textcontent : chapter_seq REFERENCESchapter_seq : chapter chapter_seqchapter_seq : chapterchapter : CHAPTER_MARK ctextctext : YEAR ctextctext : NUMBER ctextctext : REFERENCE_B ctextctext : GENERAL ctextctext : IEEE ctextctext : references : reference_seq ctextreference_seq : REFERENCE_B reference_seqreference_seq : text reference_seqreference_seq : titleandauthor : texttext : GENERAL texttext : code texttext : GENERALtext : '
    
_lr_action_items = {'INDEX':([3,5,14,16,32,34,35,47,],[-5,-4,-27,-26,-25,-24,-27,51,]),'TERMS':([3,5,14,16,32,34,36,37,48,51,],[-5,-4,-27,-26,-25,-24,-27,-27,52,-7,]),'CHAPTER_MARK':([3,4,5,10,11,14,16,21,22,23,24,25,26,32,34,38,39,40,41,42,49,50,52,53,],[-5,11,-4,11,-18,-27,-26,-18,-18,-18,-12,-18,-18,-25,-24,-14,-16,-13,-17,-15,-2,-3,-27,-8,]),'ABSTRACT':([3,5,8,9,14,16,17,18,19,32,34,46,],[-5,-4,-27,-27,-27,-26,-23,35,35,-25,-24,-6,]),'NUMBER':([0,2,3,5,7,8,9,11,12,14,16,21,22,23,25,26,27,28,30,31,32,34,35,36,37,44,45,46,51,52,],[3,3,-5,-4,3,3,3,21,3,3,3,21,21,21,21,21,21,3,3,-9,-25,-24,3,3,3,-21,-20,-6,-7,3,]),'MONTH':([3,5,7,14,15,16,32,34,],[-5,-4,-27,-27,33,-26,-25,-24,]),'REFERENCE_B':([3,5,11,12,14,16,21,22,23,25,26,27,28,30,31,32,34,44,45,],[-5,-4,26,30,-27,-26,26,26,26,26,26,26,30,30,-9,-25,-24,-21,-20,]),'REFERENCES':([10,11,13,20,21,22,23,24,25,26,38,39,40,41,42,],[-11,-18,31,-10,-18,-18,-18,-12,-18,-18,-14,-16,-13,-17,-15,]),'YEAR':([0,2,3,5,7,8,9,11,12,14,16,21,22,23,25,26,27,28,30,31,32,33,34,35,36,37,44,45,46,51,52,],[5,5,-5,-4,5,5,5,23,5,5,5,23,23,23,23,23,23,5,5,-9,-25,46,-24,5,5,5,-21,-20,-6,-7,5,]),'GENERAL':([3,5,7,8,9,11,12,14,16,21,22,23,25,26,27,28,30,31,32,34,35,36,37,44,45,46,51,52,],[-5,-4,16,16,16,22,16,16,16,22,22,22,22,22,22,16,16,-9,-25,-24,16,16,16,-21,-20,-6,-7,16,]),'IEEE':([0,1,3,5,11,12,14,16,21,22,23,25,26,27,28,30,31,32,34,44,45,],[7,7,-5,-4,25,-22,-27,-26,25,25,25,25,25,25,-22,-22,-9,-25,-24,-21,-20,]),'$end':([3,5,6,12,14,16,21,22,23,25,26,27,28,29,30,31,32,34,38,39,40,41,42,43,44,45,],[-5,-4,0,-22,-27,-26,-18,-18,-18,-18,-18,-18,-22,-1,-22,-9,-25,-24,-14,-16,-13,-17,-15,-19,-21,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'chapter':([4,10,],[10,10,]),'reference_seq':([12,28,30,],[27,44,45,]),'code':([0,2,7,8,9,12,14,16,28,30,35,36,37,52,],[1,9,14,14,14,14,14,14,14,14,14,14,14,14,]),'publication':([0,1,],[2,8,]),'text':([7,8,9,12,14,16,28,30,35,36,37,52,],[15,17,17,28,32,34,28,28,47,48,48,53,]),'abstract':([18,19,],[36,37,]),'titleandauthor':([8,9,],[18,19,]),'content':([4,],[12,]),'header':([0,],[4,]),'references':([12,],[29,]),'keywords':([36,37,],[49,50,]),'article':([0,],[6,]),'ctext':([11,21,22,23,25,26,27,],[24,38,39,40,41,42,43,]),'chapter_seq':([4,10,],[13,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> article","S'",1,None,None,None),
  ('article -> header content references','article',3,'p_article','parser.py',12),
  ('header -> code publication titleandauthor abstract keywords','header',5,'p_header_code','parser.py',18),
  ('header -> publication code titleandauthor abstract keywords','header',5,'p_header_pub','parser.py',24),
  ('code -> YEAR','code',1,'p_code','parser.py',30),
  ('code -> NUMBER','code',1,'p_code_number','parser.py',35),
  ('publication -> IEEE text MONTH YEAR','publication',4,'p_publication','parser.py',40),
  ('abstract -> ABSTRACT text INDEX','abstract',3,'p_abstract','parser.py',45),
  ('keywords -> text TERMS text','keywords',3,'p_keywords','parser.py',50),
  ('content -> chapter_seq REFERENCES','content',2,'p_content','parser.py',55),
  ('chapter_seq -> chapter chapter_seq','chapter_seq',2,'p_chapter_seq_r','parser.py',61),
  ('chapter_seq -> chapter','chapter_seq',1,'p_chapter_seq','parser.py',66),
  ('chapter -> CHAPTER_MARK ctext','chapter',2,'p_chapter','parser.py',71),
  ('ctext -> YEAR ctext','ctext',2,'p_ctext_year','parser.py',77),
  ('ctext -> NUMBER ctext','ctext',2,'p_ctext_number','parser.py',82),
  ('ctext -> REFERENCE_B ctext','ctext',2,'p_ctext_reference','parser.py',87),
  ('ctext -> GENERAL ctext','ctext',2,'p_ctext_text','parser.py',92),
  ('ctext -> IEEE ctext','ctext',2,'p_ctext_ieee','parser.py',97),
  ('ctext -> <empty>','ctext',0,'p_ctext','parser.py',102),
  ('references -> reference_seq ctext','references',2,'p_references','parser.py',107),
  ('reference_seq -> REFERENCE_B reference_seq','reference_seq',2,'p_reference_seq_B','parser.py',112),
  ('reference_seq -> text reference_seq','reference_seq',2,'p_reference_seq_general','parser.py',122),
  ('reference_seq -> <empty>','reference_seq',0,'p_reference_seq','parser.py',127),
  ('titleandauthor -> text','titleandauthor',1,'p_titleandauthor','parser.py',132),
  ('text -> GENERAL text','text',2,'p_text_general','parser.py',137),
  ('text -> code text','text',2,'p_text_number','parser.py',142),
  ('text -> GENERAL','text',1,'p_text','parser.py',147),
  ('text -> <empty>','text',0,'p_text_none','parser.py',152),
]
