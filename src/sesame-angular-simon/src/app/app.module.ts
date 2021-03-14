import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FullCalendarModule } from '@fullcalendar/angular';
import dayGridPlugin from '@fullcalendar/daygrid';
//import timeGridPlugin from '@fullcalendar/timegrid';
//import listPlugin from '@fullcalendar/list';
//import interactionPlugin from '@fullcalendar/interaction';
import { AppComponent } from './app.component';
import { MenuComponent } from './menu/menu.component';
import { HeaderComponent } from './header/header.component';
import { ProfilepictureUsernameComponent } from './profilepicture-username/profilepicture-username.component';
import { EntrylistComponent } from './entrylist/entrylist.component';
import { HomeComponent } from './home/home.component';
import { GalleryComponent } from './gallery/gallery.component';
import { LiveComponent } from './live/live.component';
import { SettingsComponent } from './settings/settings.component';
import { ProfileComponent } from './profile/profile.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { RouterModule } from '@angular/router';
import { RoutingModule } from './routing/routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MdbModule } from 'mdb-angular-ui-kit';
import { FlexLayoutModule } from "@angular/flex-layout";


FullCalendarModule.registerPlugins([
  dayGridPlugin
])

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    HeaderComponent,
    ProfilepictureUsernameComponent,
    EntrylistComponent,
    HomeComponent,
    GalleryComponent,
    LiveComponent,
    SettingsComponent,
    ProfileComponent,
    LoginComponent,
    RegisterComponent,
    ForgotPasswordComponent
  ],
  imports: [
    BrowserModule,
    FullCalendarModule,
    RouterModule.forRoot([
      { path: "home", component: HomeComponent },
      { path: '', redirectTo: '/home', pathMatch: 'full' },
      { path: "settings", component: SettingsComponent },
      { path: "gallery", component: GalleryComponent },
      { path: "profile", component: ProfileComponent },
      { path: "live", component: LiveComponent },
      { path: "register", component: RegisterComponent },
      { path: "login", component: LoginComponent },
      { path: "forgot", component: ForgotPasswordComponent }
    ]),
    RoutingModule,
    BrowserAnimationsModule,
    MdbModule,   
    FlexLayoutModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
