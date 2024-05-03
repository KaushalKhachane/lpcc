%{
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
extern int yylex();
extern void yyerror(const char *s);

char *convert_case(char *str) {
    int length = strlen(str);
    for (int i = 0; i < length; i++) {
        if (islower(str[i]))
            str[i] = toupper(str[i]);
        else if (isupper(str[i]))
            str[i] = tolower(str[i]);
    }
    return str;
}
%}

%union {
    int ival;
    char *sval;
}

%token <sval> STRING
%token <ival> NUMBER
%type <sval> expr
%type <sval> var

%%

program:
    statement { printf("\n"); }
    | program statement { printf("\n"); }
    ;

statement:
    var '=' expr { printf("%s = %s\n", $1, convert_case($3)); }
    ;

var:
    'u' { $$ = "u"; }
    | 'v' { $$ = "v"; }
    ;

expr:
    STRING { $$ = $1; }
    | NUMBER { $$ = ""; }
    ;

%%

int main(void) {
    printf("Enter expressions like 'u = string' or 'v = string':\n");
    return yyparse();
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
