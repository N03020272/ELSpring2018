import { Component, OnInit } from '@angular/core';


export class InstallComponent{
    constructor(){ }



     save(){
         var gidNumber = document.getElementById("gidNumber").nodeValue;
        console.log(gidNumber);
    }
}
