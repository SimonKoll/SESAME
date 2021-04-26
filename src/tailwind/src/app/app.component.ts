import { Component, OnInit } from '@angular/core';
import * as data from '../assets/entries.json';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'Sesame';

  entries:any = data;

  
  ngOnInit(): void{}

  onOpenProfile() {
    var desktopMenu =  document.getElementById("menu");
    
    if (desktopMenu.style.visibility === 'hidden') {
      desktopMenu.style.visibility = 'visible';
    } else {
      desktopMenu.style.visibility = 'hidden'
    }

  }

}

