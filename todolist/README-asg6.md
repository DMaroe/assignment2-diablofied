Name : Dylan Dahran Pribadi
NPM  : 2106720872

1. Describe the difference between asynchronous programming with synchronous programming.

Asynchronous programming, conversely, is a multithreaded model that’s most applicable to networking and communications. Asynchronous is a non-blocking architecture, which means it doesn’t block further execution while one or more operations are in progress.

With asynchronous programming, multiple related operations can run concurrently without waiting for other tasks to complete. During asynchronous communication, parties receive and process messages when it’s convenient or possible to do so, rather than responding immediately upon receipt.

Synchronous is known as a blocking architecture and is ideal for programming reactive systems. As a single-thread model, it follows a strict set of sequences, which means that operations are performed one at a time, in perfect order. While one operation is being performed, other operations’ instructions are blocked. The completion of the first task triggers the next, and so on.

To illustrate how synchronous programming works, think of a telephone. During a phone call, while one person speaks, the other listens. When the first person finishes, the second tends to respond immediately.

2. When Implementing JavaScript and AJAX, there is an application in the paradigms of Event-Driven Programming. Describe the reasoning for those paradigms and state some examples of its application.

Event Driven Programming is a programming paradigm in which objects can communicate indirectly by sending messages to one another through intermediaries. The message is sent via an event stream. 

This paradigm depends on events by paying attention to what operations will be implemented from the existence of events. The application of the paradigm in this task is found in the implementation of the submit form button for adding tasks. 

3. Describe the implementation of asynchronous programming in AJAX.

Asynchronous programming is a programming paradigm that allows a program to perform multiple tasks concurrently, rather than sequentially. In the context of AJAX (Asynchronous JavaScript and XML), asynchronous programming is used to make requests to a server without blocking the execution of the rest of the program.

One way to implement asynchronous programming in AJAX is to use the XMLHttpRequest object, which allows a web page to make requests to a server without reloading the page. To make an asynchronous request, you can use the XMLHttpRequest object's "open" method to specify the URL of the resource to be requested and set the "async" parameter to "true". Then, you can use the "send" method to send the request.

4. Explain how you would implement the checklist above.