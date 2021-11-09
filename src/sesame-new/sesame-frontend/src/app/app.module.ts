import * as $ from 'jquery';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {CommonModule, LocationStrategy} from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { Routes, RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FullComponent } from './layouts/full/full.component';
import { NavigationComponent } from './shared/header-navigation/navigation.component';
import { SidebarComponent } from './shared/sidebar/sidebar.component';
import { BreadcrumbComponent } from './shared/breadcrumb/breadcrumb.component';
import { Approutes } from './app-routing.module';
import { AppComponent } from './app.component';
import { SpinnerComponent } from './shared/spinner.component';
import { MatTableModule } from '@angular/material/table';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';

@NgModule({
	declarations: [
		AppComponent,
		SpinnerComponent,
		FullComponent,
		NavigationComponent,
		BreadcrumbComponent,
		SidebarComponent,
	],
	imports: [
		CommonModule,
		BrowserModule,
		BrowserAnimationsModule,
		FormsModule,
		HttpClientModule,
		NgbModule,
		MatInputModule,
		MatTableModule,
		MatFormFieldModule,
		RouterModule.forRoot(Approutes, { useHash: false, relativeLinkResolution: 'legacy' })
	],
	exports: [MatFormFieldModule, MatInputModule, BrowserAnimationsModule],
	bootstrap: [AppComponent]
})
export class AppModule { }
