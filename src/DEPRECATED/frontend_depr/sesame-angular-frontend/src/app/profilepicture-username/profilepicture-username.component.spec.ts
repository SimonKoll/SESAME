import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfilepictureUsernameComponent } from './profilepicture-username.component';

describe('ProfilepictureUsernameComponent', () => {
  let component: ProfilepictureUsernameComponent;
  let fixture: ComponentFixture<ProfilepictureUsernameComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProfilepictureUsernameComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfilepictureUsernameComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
