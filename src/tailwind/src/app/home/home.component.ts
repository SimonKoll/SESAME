import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    var navbar = document.getElementById("navbar")
    navbar.style.height = "64px"
  }
  onOpenProfile() {
    var desktopMenu =  document.getElementById("menu");
    
    if (desktopMenu.style.visibility === 'hidden') {
      desktopMenu.style.visibility = 'visible';
    } else {
      desktopMenu.style.visibility = 'hidden'
    }

  }
  onClickBurger(){
    var mobileMenu =  document.getElementById("mobile-menu");
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
