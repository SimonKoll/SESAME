import { Component, AfterViewInit } from '@angular/core';


declare var require: any;

@Component({
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})

export class DashboardComponent implements AfterViewInit {
  subtitle = '';
  constructor() {
    this.subtitle = 'This is some text within a card block.';
  }

  ngAfterViewInit() { }
}
