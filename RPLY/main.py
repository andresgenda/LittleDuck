from LittleDuckLexer import Lexer
from LittleDuckParser import Parser

text_input = """
program myProgram2;
var x, y, z : float;
{
   x = 2;
   print("Bienvenido al programa ", x);
   if(x <> 2){
       y = x + 1;
       z = y;
   };
   print(x, y, z);
}
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
print("EXITO")