import { BrowserModule, Title } from '@angular/platform-browser';
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
      { path: "home", component: HomeComponent , data:{title: 'Home'}},
      { path: '', redirectTo: '/home', pathMatch: 'full' ,data:{title: 'Home'}},
      { path: "settings", component: SettingsComponent ,data:{title: 'Settings'}},
      { path: "gallery", component: GalleryComponent ,data:{title: 'Gallery'}},
      { path: "profile", component: ProfileComponent,data:{title: 'Profile'} },
      { path: "live", component: LiveComponent ,data:{title: 'Live'}},
      { path: "register", component: RegisterComponent ,data:{title: 'Register'}},
      { path: "login", component: LoginComponent,data:{title: 'Login'} },
      { path: "forgot", component: ForgotPasswordComponent,data:{title: 'Forgot Password'} },
      { path: "list", component: EntrylistComponent ,data:{title: 'EntryList'}}
    ]),
    RoutingModule,
    BrowserAnimationsModule,
    MdbModule,   
    FlexLayoutModule
  ],
  providers: [Title],
  bootstrap: [AppComponent]
})
export class AppModule {
  title = 'angulartitle';

  constructor(private titleService: Title) {}

  setDocTitle(title: string) {
     console.log('current title:::::' + this.titleService.getTitle());
     this.titleService.setTitle(title);
  }
 }
