def main():
    uni_list = {
        "UPN":{
        "careers" : "4",
        "cost" : "Inscripción/Reinscripción semestral: Aproximadamente entre $715.00 y $3,300.00 pesos mexicanos, dependiendo del año y la modalidad (presencial o en línea).",
        "nearest one" : "26km"
    }, 
        "URN":{
        "careers" : "7",
        "cost" : "$3,600.00 MXN al mes aproximadamente",
        "nearest one" : "25km"
    }, 
        "UACJ":{
        "careers" : "8",
        "cost" : "$5,200 pesos mexicanos aproximadamenbte.",
        "nearest one" : "35km"
    }, 
        "elpac":{
        "careers" : "1",
        "cost" : " de $4,300 pesos de inscripción por semestre y $3,500 pesos de colegiatura mensual.",
        "nearest one" : "318km"
    }, 
        "ISAC":{
        "careers" : "2",
        "cost" : "aproximado por semestre de $100,000 MXN en colegiatura.",
        "nearest one" : "310km"
    }

}
    print("The universities we have information rigth now are:")
    list=["UPN", "URN", "UACJ", "elpac", "ISAC"]
    print(list)
    uni= input("About what university did you want to have information: ")
    

    if uni in uni_list:
        info = uni_list[uni] 
        print(info)
main()