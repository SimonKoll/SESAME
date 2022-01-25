import { Component, OnInit } from "@angular/core";
import { MatTableDataSource } from "@angular/material/table";
import entries from "../../../../assets/entries.json";
import { MatTableModule } from "@angular/material/table";
import { Entrant } from "src/app/entrant.model";
import { HttpserviceService } from "src/app/httpservice.service";
import { Observable } from "rxjs";

@Component({
  selector: "entries-list",
  templateUrl: "./entries-list.component.html",
  styleUrls: ["./entries-list.component.css"],
})
export class EntriesListComponent implements OnInit {
  displayedColumns: string[] = ["Name", "Time"];
  entryList: Entrant[] = [];
  entrant: string | undefined;
  entryDataSource!: MatTableDataSource<Entrant>;
  entryListEdited: { name: String; time: String } | undefined;

  constructor(private httpservice: HttpserviceService) {}

  ngOnInit(): void {
    this.loadCustomers();
  }

  loadCustomers() {
    this.httpservice.getEntrants().subscribe((data: Entrant[]) => {
      this.entryList = data;
      console.log("entrylist:" + this.entryList);
      this.entryDataSource = new MatTableDataSource(this.entryList)
      console.log(this.entryDataSource)
    });
  }
}
