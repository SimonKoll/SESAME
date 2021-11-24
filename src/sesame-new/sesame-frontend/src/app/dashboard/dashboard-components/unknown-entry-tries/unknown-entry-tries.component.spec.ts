import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { UnknownEntryTriesComponent } from './unknown-entry-tries.component';

describe('LatestSalesComponent', () => {
  let component: UnknownEntryTriesComponent;
  let fixture: ComponentFixture<UnknownEntryTriesComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ UnknownEntryTriesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UnknownEntryTriesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
