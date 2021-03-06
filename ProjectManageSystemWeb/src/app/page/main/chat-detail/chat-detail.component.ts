import { Component, OnInit, Input } from '@angular/core';
import { Chat } from '../../../system/chat_module/chat';

@Component({
  selector: 'app-chat-detail',
  templateUrl: './chat-detail.component.html',
  styleUrls: ['./chat-detail.component.css']
})

export class ChatDetailComponent implements OnInit {

  @Input() msgList: Chat;

  constructor() {
  }

  ngOnInit() {
  }

}
