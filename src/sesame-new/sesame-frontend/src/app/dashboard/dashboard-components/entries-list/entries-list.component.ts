import io from 'socket.io-client';
import { Component, OnInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import entries from '../../../../assets/entries.json';
import { MatTableModule } from '@angular/material/table';
import { Entrant } from 'src/app/entrant.model';

@Component({
  selector: 'entries-list',
  templateUrl: './entries-list.component.html',
  styleUrls: ['./entries-list.component.css']
})

export class EntriesListComponent implements OnInit {
  socket = io('http://localhost:4000');
  
  displayedColumns: string[] = ['Name', 'Time'];
  entryList: {name: String; time: String }[] = entries['recognized-entries'];
  entryDataSource = new MatTableDataSource(this.entryList.slice(0, 5));
  entrant: string | undefined;
  entryListEdited: { name: String; time: String; } | undefined;

  constructor(private api: ApiService) { }

  ngOnInit(): void {
  }

  getEntrants() {
    this.api.getSales()
    .subscribe((res: any) => {
      this.data = res;
      console.log(this.data);
      this.isLoadingResults = false;
    }, err => {
      console.log(err);
      this.isLoadingResults = false;
    });
  }

}
