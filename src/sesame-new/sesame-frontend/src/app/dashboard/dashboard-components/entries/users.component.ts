import { Component, OnInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import entries from '../../../../assets/entries.json';
import { MatTableModule } from '@angular/material/table';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})

export class UsersComponent implements OnInit {
  displayedColumns: string[] = ['Name', 'Time'];
  entryList: {name: String; time: String }[] = entries['recognized-entries'];
  entryDataSource = new MatTableDataSource(this.entryList);
  entrant: string | undefined;
  entryListEdited: { name: String; time: String; } | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}
