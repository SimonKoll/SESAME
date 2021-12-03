import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';


import { ComponentsRoutes } from './component.routing';
import { EntryComponent } from './entry/entry.component';
import { LiveComponent } from './live/live.component';
import { ProfileComponent } from './profile/profile.component';
import { AccessmanagementComponent } from './access-management/accessmanagement.component';
import { MatTableModule } from '@angular/material/table';

@NgModule({
  imports: [
    CommonModule,
    MatTableModule,
    RouterModule.forChild(ComponentsRoutes)
  ],
  declarations: [
    EntryComponent,
    LiveComponent,
    ProfileComponent,
    AccessmanagementComponent
  ]
})
export class ComponentsModule {}
