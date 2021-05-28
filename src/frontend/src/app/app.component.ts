import { Component, OnInit } from '@angular/core';
import * as data from '../assets/entries.json';
import {MatFormFieldModule} from '@angular/material/form-field';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'Sesame';

  entries: any = data;


  ngOnInit(): void { }

  onOpenProfile() {
    var desktopMenu = document.getElementById("menu");

    if (desktopMenu.style.visibility === 'hidden') {
      desktopMenu.style.visibility = 'visible';
    } else {
      desktopMenu.style.visibility = 'hidden'
    }
  }
  onClickBurger() {
    var mobileMenu = document.getElementById("mobile-menu");
    mobileMenu
    var navbar = document.getElementById("navbar")
    if (mobileMenu.style.visibility === 'hidden') {
      mobileMenu.style.visibility = 'visible';
      navbar.style.height = "509px"
    } else {
      mobileMenu.style.visibility = 'hidden'
      navbar.style.height = "64px"

    }
  }

}


