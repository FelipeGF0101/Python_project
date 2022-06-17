'''
Dunder Name e Dunder Main

Dunder -> Double Underscore

Dunder Name -> __name__

Dunder Main -> __main__

Em Python são utilizados dunder para criar funções, atributos, propriedades e etc, utilizando Double Underscore para não gerar conflito com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:

int main(){
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:
public static void main (String[] args){

}

# Em python se executarmos um módulo python diretamente na linha de comando, internamente o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

-> Main: Significa 'principal' 

from Funções_com_parâmetros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6]))

'''
import primeiro, segundo