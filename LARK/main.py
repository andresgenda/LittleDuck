from lark import Lark, Transformer, v_args

grammar = """
	programa: PROGRAM ID SEMI_COLON programa2
	programa2: vars bloque | bloque
	vars: VAR vars2
	vars2: ID COMMA vars2 | ID COLON tipo SEMI_COLON
	tipo: INT | FLOAT
	bloque: OPEN_BRACK bloque2
	bloque2: estatuto bloque2 | estatuto CLOSE_BRACK
	estatuto: asignacion | condicion | escritura
	asignacion: ID EQUAL expresion SEMI_COLON
	condicion: IF OPEN_PARENTH expresion CLOSE_PARENTH bloque condicion2
	condicion2: ELSE bloque condicion3 | condicion3
	condicion3: SEMI_COLON
	escritura: PRINT OPEN_PARENTH escritura2
	escritura2: expresion escritura3 | CTE_STRING escritura3
	escritura3: COMMA escritura2 | CLOSE_PARENTH SEMI_COLON
	expresion: exp expresion2 | expresion3
	expresion2: MORE_THAN expresion3 | LESS_THAN expresion3 | NOT_EQUAL expresion3
	expresion3: exp
	exp: termino ADD exp | termino SUBSTR exp | termino
	termino: factor MULT termino | factor DIVIS termino | factor
	factor: OPEN_PARENTH expresion CLOSE_PARENTH | factor2 |factor3
	factor2: ADD factor3 | SUBSTR factor3
	factor3: varcte
	varcte: ID |CTE_INT | CTE_FLOAT

	PROGRAM: "program"
	PRINT: "print"
	SEMI_COLON: ";"
	VAR: "var"
	COMMA: ","
	COLON: ":"
	INT: "int"
	FLOAT: "float"
	OPEN_BRACK: "{"
	CLOSE_BRACK: "}"
	EQUAL: "="
	IF: "if"
	ELSE: "else"
	OPEN_PARENTH: "("
	CLOSE_PARENTH: ")"
	NOT_EQUAL: "<>"
	MORE_THAN: ">"
	LESS_THAN: "<"
	ADD: "+"
	SUBSTR: "-"
	MULT: "*"
	DIVIS: "/"
	%import common.ESCAPED_STRING -> CTE_STRING
	%import common.SIGNED_INT -> CTE_INT
	%import common.SIGNED_FLOAT -> CTE_FLOAT
	%import common.CNAME -> ID
	%import common.LETTER
    %import common.WS_INLINE
    %import common.WS
    %ignore WS
    %ignore WS_INLINE
    %ignore " "
"""

def main():
    calc_parser = Lark(grammar, parser='lalr', start="programa")
    calc = calc_parser.parse
    try:
        if(calc("""
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
""")):
            print("EXITO!")
    except Exception as ex:
        print("NO EXITO", ex)

if __name__ == '__main__':
    main()