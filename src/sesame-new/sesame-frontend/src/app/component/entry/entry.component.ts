import { Component } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import entries from '../../../assets/entries.json';
import { MatTableModule } from '@angular/material/table';

@Component({
	selector: 'entry',
	templateUrl: 'entry.component.html',
	styleUrls: ['./entry.component.css']
})

export class EntryComponent {
	displayedColumns: string[] = ['Name', 'Time'];
	entryList: {name: String; time: String }[] = entries['recognized-entries'];
	entryDataSource = new MatTableDataSource(this.entryList);
	entrant: string | undefined;
	entryListEdited: { name: String; time: String; } | undefined;

}
