import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { EntriesComponent } from './entries/entries.component';
import { SettingsComponent } from './settings/settings.component';
import { ProfileComponent } from './profile/profile.component';
import { LiveComponent } from './live/live.component';
import { LoginComponent } from './login/login.component';
import { LoginRegisterComponent } from './login-register/login-register.component';
import { GalleryComponent } from './gallery/gallery.component';
import { ProfilepicUsernameComponent } from './profilepic-username/profilepic-username.component';
import { ForgotComponent } from './forgot/forgot.component';
import { NavSideComponent } from './nav-side/nav-side.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    EntriesComponent,
    SettingsComponent,
    ProfileComponent,
    LiveComponent,
    LoginComponent,
    LoginRegisterComponent,
    GalleryComponent,
    ProfilepicUsernameComponent,
    ForgotComponent,
    NavSideComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
