style_blue_binary="""
QPushButton { 
    background-color: rgb(215, 215, 215); 
    color:rgb(89, 167, 245); 
    border: 1px solid gray; 
} QPushButton:pressed { 
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1, 
        stop: 0 #FF7832, stop: 1 #FF9739); }"""

style_blue_equals="""
QPushButton {
    background-color: rgb(89, 167, 245);
    color: white; 
	border: 1px solid gray;
} QPushButton:pressed { 
    background-color: qlineargradient(
    x1: 0, y1: 0, x2: 0, y2: 1, 
	stop: 0 #FF7832, stop: 1 #FF9739); }"""

style_blue_clear="""
QPushButton { 
    color: rgb(232, 119, 88);
    background-color: rgb(215, 215, 215);
 	border: 1px solid gray;
} QPushButton:pressed { 
    background-color: qlineargradient(
    x1: 0, y1: 0, x2: 0, y2: 1, 
 	stop: 0 #BEBEBE, stop: 1 #D7D7D7); }"""

style_orange_binary="""
QPushButton { 
    background-color: rgb(255, 151, 57); 
    color: white;
    border: 1px solid gray; 
} QPushButton:pressed { 
    background-color:qlineargradient(
    x1: 0, y1: 0, x2: 0, y2: 1,
     stop: 0 #FF7832, stop: 1 #FF9739); }"""

style_orange_unary=""" 
QPushButton { 
    background-color: rgb(215, 215, 215); 
    border: 1px solid gray;
} QPushButton:pressed { 
    background-color: qlineargradient(
    x1: 0, y1: 0, x2: 0,y2: 1,
     stop: 0 #BEBEBE, stop: 1 #D7D7D7); }"""