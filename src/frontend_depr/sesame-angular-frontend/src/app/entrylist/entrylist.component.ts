import { Component } from '@angular/core';
//import { CalendarOptions, DateSelectArg, EventClickArg, EventApi } from '@fullcalendar/angular';
//import { INITIAL_EVENTS, createEventId } from './event-utils';
import entries from '../../assets/entries.json';


@Component({
  selector: 'app-entrylist',
  templateUrl: './entrylist.component.html',
  styleUrls: ['./entrylist.component.css']
})
export class EntrylistComponent {
  entryList:{name:String, time:String}[]=entries["recognized-entries"];
  
}
