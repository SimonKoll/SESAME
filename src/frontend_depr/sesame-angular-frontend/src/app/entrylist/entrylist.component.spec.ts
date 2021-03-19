import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EntrylistComponent } from './entrylist.component';

describe('EntrylistComponent', () => {
  let component: EntrylistComponent;
  let fixture: ComponentFixture<EntrylistComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EntrylistComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EntrylistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
