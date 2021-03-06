import { Component, OnInit } from '@angular/core';
import { KeycloakService } from 'keycloak-angular';
import { MatTableModule } from '@angular/material/table/';
import { MatFormFieldModule } from '@angular/material/form-field';

import { MatTableDataSource } from '@angular/material/table';

import entries from '../../assets/entries.json';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {

  displayedColumns: string[] = ['ID', 'Name', 'Time'];
  entryList: { id: Number; name: String; time: String }[] =
    entries['recognized-entries'];
  dataSource = new MatTableDataSource(this.entryList);
  entrant: string;
  entryListEdited: { id: Number; name: String; time: String };
  constructor(private keycloakService: KeycloakService) {}

  removeEntrant(id) {
    for (let i = 0; i < this.entryList.length; ++i) {
      if (this.entryList[i].id === id) {
        this.entryList.splice(i, 1);
      }
    }
  }
  ngOnInit(): void {}

  onOpenProfile() {
    var desktopMenu = document.getElementById('menu');

    if (desktopMenu.style.visibility === 'hidden') {
      desktopMenu.style.visibility = 'visible';
    } else {
      desktopMenu.style.visibility = 'hidden';
    }
  }
  onClickBurger() {
    var mobileMenu = document.getElementById('mobile-menu');
    var navbar = document.getElementById('navbar');
    if (mobileMenu.style.visibility === 'hidden') {
      mobileMenu.style.visibility = 'visible';
      navbar.style.height = '509px';
    } else {
      mobileMenu.style.visibility = 'hidden';
      navbar.style.height = '64px';
    }
  }
  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

  public username(): string {
    return this.keycloakService.getUsername();
  }
  public logout() {
    this.keycloakService.logout();
  }
}
